from estruturas.lse import ListaSimplesmenteEncadeada
from estruturas.lde import ListaDuplamenteEncadeada
from estruturas.fila import Fila
from estruturas.pilha import Pilha
from models.cliente import Cliente
from models.produto import Produto
from models.venda import Venda, ItemVenda
from algoritmos.ordenacao import insertion_sort
from algoritmos.busca_binaria import busca_binaria
from services.persistencia_service import PersistenciaService


class Estoque:
    def __init__(self):
        self.clientes = ListaSimplesmenteEncadeada()
        self.produtos = ListaDuplamenteEncadeada()
        self.vendas = Fila()
        self.historico = Pilha()
        self.persistencia = PersistenciaService()

        self._proximo_id_cliente = 1
        self._proximo_id_produto = 1
        self._proximo_id_venda = 1

        self._carregar_dados_iniciais()

    
    def _carregar_dados_iniciais(self):
        for cliente in self.persistencia.carregar_clientes():
            self.clientes.inserir(cliente)
            self._proximo_id_cliente = max(self._proximo_id_cliente, cliente.id + 1)

        for produto in self.persistencia.carregar_produtos():
            self.produtos.inserir(produto)
            self._proximo_id_produto = max(self._proximo_id_produto, produto.id + 1)

        for venda in self.persistencia.carregar_vendas():
            self.vendas.enfileirar(venda)
            self._proximo_id_venda = max(self._proximo_id_venda, venda.id + 1)

    def _salvar_tudo(self):
        self.persistencia.salvar_clientes(self.clientes.listar())
        self.persistencia.salvar_produtos(self.produtos.listar_inicio_fim())
        self.persistencia.salvar_vendas(self.vendas.listar())

   
    def cadastrar_cliente(self, nome):
        nome = nome.strip()
        if not nome:
            raise ValueError("O nome do cliente não pode ser vazio.")
        cliente = Cliente(self._proximo_id_cliente, nome)
        self.clientes.inserir(cliente)
        self._proximo_id_cliente += 1
        self.historico.empilhar({"tipo": "cadastrar_cliente", "cliente": cliente})
        self._salvar_tudo()
        return cliente

    def listar_clientes(self):
        return self.clientes.listar()

    def buscar_cliente(self, id_cliente):
        return self.clientes.buscar(id_cliente)

    def remover_cliente(self, id_cliente):
        cliente = self.clientes.remover(id_cliente)
        if cliente is None:
            raise ValueError(f"Cliente com ID {id_cliente} não existe.")
        self.historico.empilhar({"tipo": "remover_cliente", "cliente": cliente})
        self._salvar_tudo()
        return cliente

    
    def cadastrar_produto(self, nome, quantidade, preco):
        nome = nome.strip()
        if not nome:
            raise ValueError("O nome do produto não pode ser vazio.")
        if preco <= 0:
            raise ValueError("O preço deve ser maior que zero.")
        if quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        produto = Produto(self._proximo_id_produto, nome, quantidade, preco)
        self.produtos.inserir(produto)
        self._proximo_id_produto += 1
        self.historico.empilhar({"tipo": "cadastrar_produto", "produto": produto})
        self._salvar_tudo()
        return produto

    def listar_produtos_inicio_fim(self):
        return self.produtos.listar_inicio_fim()

    def listar_produtos_fim_inicio(self):
        return self.produtos.listar_fim_inicio()

    def buscar_produto(self, id_produto):
        return self.produtos.buscar(id_produto)

    def remover_produto(self, id_produto):
        produto = self.produtos.remover(id_produto)
        if produto is None:
            raise ValueError(f"Produto com ID {id_produto} não existe.")
        self.historico.empilhar({"tipo": "remover_produto", "produto": produto})
        self._salvar_tudo()
        return produto

    def atualizar_estoque(self, id_produto, nova_quantidade):
        produto = self.produtos.buscar(id_produto)
        if produto is None:
            raise ValueError(f"Produto com ID {id_produto} não existe.")
        if nova_quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")
        quantidade_antiga = produto.quantidade
        produto.quantidade = nova_quantidade
        self.historico.empilhar({
            "tipo": "atualizar_estoque",
            "produto_id": id_produto,
            "quantidade_antiga": quantidade_antiga,
        })
        self._salvar_tudo()
        return produto

    
    def produtos_ordenados_por_id(self):
        auxiliar = self.produtos.para_lista_auxiliar()
        return insertion_sort(auxiliar, chave=lambda p: p.id, crescente=True)

    def buscar_produto_binaria(self, id_produto):
        ordenados = self.produtos_ordenados_por_id()
        return busca_binaria(ordenados, id_produto, chave=lambda p: p.id)

    
    def realizar_venda(self, id_cliente, itens_solicitados):
        """
        itens_solicitados: lista de tuplas (id_produto, quantidade)
        Valida tudo antes de alterar qualquer dado.
        """
        cliente = self.clientes.buscar(id_cliente)
        if cliente is None:
            raise ValueError(f"Cliente com ID {id_cliente} não está cadastrado.")

        if not itens_solicitados:
            raise ValueError("A venda precisa ter pelo menos um produto.")

        produtos_validados = []
        for id_produto, quantidade in itens_solicitados:
            if not isinstance(quantidade, int) or quantidade <= 0:
                raise ValueError(f"Quantidade inválida para o produto {id_produto}.")
            produto = self.produtos.buscar(id_produto)
            if produto is None:
                raise ValueError(f"Produto com ID {id_produto} não existe.")
            if produto.quantidade < quantidade:
                raise ValueError(
                    f"Estoque insuficiente para o produto '{produto.nome}' "
                    f"(disponível: {produto.quantidade}, solicitado: {quantidade})."
                )
            produtos_validados.append((produto, quantidade))

        
        itens_venda = []
        for produto, quantidade in produtos_validados:
            produto.quantidade -= quantidade
            itens_venda.append(ItemVenda(produto.id, quantidade, produto.preco))

        venda = Venda(self._proximo_id_venda, id_cliente, itens_venda)
        self._proximo_id_venda += 1
        self.vendas.enfileirar(venda)

        self.historico.empilhar({"tipo": "realizar_venda", "venda": venda})
        self._salvar_tudo()
        return venda

    def visualizar_fila_vendas(self):
        return self.vendas.listar()

    def ver_primeira_venda(self):
        return self.vendas.ver_primeiro()

    
    def desfazer_ultima_operacao(self):
        operacao = self.historico.desempilhar()
        if operacao is None:
            raise ValueError("Não há operações para desfazer.")

        tipo = operacao["tipo"]

        if tipo == "cadastrar_cliente":
            self.clientes.remover(operacao["cliente"].id)

        elif tipo == "remover_cliente":
            self.clientes.inserir_dado_bruto(operacao["cliente"])

        elif tipo == "cadastrar_produto":
            self.produtos.remover(operacao["produto"].id)

        elif tipo == "remover_produto":
            self.produtos.inserir(operacao["produto"])

        elif tipo == "atualizar_estoque":
            produto = self.produtos.buscar(operacao["produto_id"])
            if produto is not None:
                produto.quantidade = operacao["quantidade_antiga"]

        elif tipo == "realizar_venda":
            venda = operacao["venda"]
            for item in venda.itens:
                produto = self.produtos.buscar(item.produto_id)
                if produto is not None:
                    produto.quantidade += item.quantidade
            self.vendas.remover_ultimo()

        self._salvar_tudo()
        return operacao

    
    def valor_total_estoque(self):
        return sum(p.quantidade * p.preco for p in self.produtos)

    def valor_total_vendas(self):
        return sum(v.valor_total for v in self.vendas)

    def clientes_e_valores_gastos(self):
        totais = {}
        for venda in self.vendas:
            totais[venda.cliente_id] = totais.get(venda.cliente_id, 0.0) + venda.valor_total
        resultado = []
        for id_cliente, total in totais.items():
            cliente = self.clientes.buscar(id_cliente)
            nome = cliente.nome if cliente else "Cliente removido"
            resultado.append((id_cliente, nome, total))
        return resultado

    def cliente_que_mais_gastou(self):
        totais = self.clientes_e_valores_gastos()
        if not totais:
            return None
        return max(totais, key=lambda t: t[2])

    def produto_mais_vendido(self):
        quantidades = {}
        for venda in self.vendas:
            for item in venda.itens:
                quantidades[item.produto_id] = quantidades.get(item.produto_id, 0) + item.quantidade
        if not quantidades:
            return None
        id_mais_vendido = max(quantidades, key=lambda pid: quantidades[pid])
        produto = self.produtos.buscar(id_mais_vendido)
        nome = produto.nome if produto else "Produto removido"
        return (id_mais_vendido, nome, quantidades[id_mais_vendido])
