from services.estoque_service import Estoque


def ler_inteiro(mensagem):
    while True:
        texto = input(mensagem).strip()
        try:
            return int(texto)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.\n")


def ler_float(mensagem):
    while True:
        texto = input(mensagem).strip().replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Entrada inválida. Digite um número (ex: 10.50).\n")


def ler_opcao_menu():
    texto = input("Escolha uma opção: ").strip()
    try:
        return int(texto)
    except ValueError:
        
        return -1  


def exibir_menu():
    print("\n==============================")
    print(" SISTEMA DE ESTOQUE E VENDAS")
    print("==============================")
    print("1  - Cadastrar cliente")
    print("2  - Listar clientes")
    print("3  - Buscar cliente")
    print("4  - Remover cliente")
    print("5  - Cadastrar produto")
    print("6  - Listar produtos")
    print("7  - Buscar produto")
    print("8  - Atualizar estoque")
    print("9  - Remover produto")
    print("10 - Listar produtos em ordem inversa")
    print("11 - Listar produtos ordenados")
    print("12 - Buscar produto por ID usando Busca Binária")
    print("13 - Realizar venda")
    print("14 - Visualizar fila de vendas")
    print("15 - Visualizar primeira venda da fila")
    print("16 - Exibir valor total do estoque")
    print("17 - Exibir valor total das vendas")
    print("18 - Exibir clientes e valores totais gastos")
    print("19 - Exibir cliente que mais gastou")
    print("20 - Exibir produto mais vendido")
    print("21 - Desfazer última operação")
    print("0  - Sair")


def cadastrar_cliente(estoque):
    nome = input("Nome do cliente: ")
    try:
        cliente = estoque.cadastrar_cliente(nome)
        print(f"Cliente cadastrado com sucesso: {cliente}")
    except ValueError as erro:
        print(f"Erro: {erro}")


def listar_clientes(estoque):
    clientes = estoque.listar_clientes()
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for cliente in clientes:
        print(cliente)


def buscar_cliente(estoque):
    id_cliente = ler_inteiro("ID do cliente: ")
    cliente = estoque.buscar_cliente(id_cliente)
    print(cliente if cliente else "Cliente não encontrado.")


def remover_cliente(estoque):
    id_cliente = ler_inteiro("ID do cliente a remover: ")
    try:
        cliente = estoque.remover_cliente(id_cliente)
        print(f"Cliente removido: {cliente}")
    except ValueError as erro:
        print(f"Erro: {erro}")


def cadastrar_produto(estoque):
    nome = input("Nome do produto: ")
    quantidade = ler_inteiro("Quantidade em estoque: ")
    preco = ler_float("Preço: ")
    try:
        produto = estoque.cadastrar_produto(nome, quantidade, preco)
        print(f"Produto cadastrado com sucesso: {produto}")
    except ValueError as erro:
        print(f"Erro: {erro}")


def listar_produtos(estoque):
    produtos = estoque.listar_produtos_inicio_fim()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for produto in produtos:
        print(produto)


def buscar_produto(estoque):
    id_produto = ler_inteiro("ID do produto: ")
    produto = estoque.buscar_produto(id_produto)
    print(produto if produto else "Produto não encontrado.")


def atualizar_estoque(estoque):
    id_produto = ler_inteiro("ID do produto: ")
    nova_quantidade = ler_inteiro("Nova quantidade: ")
    try:
        produto = estoque.atualizar_estoque(id_produto, nova_quantidade)
        print(f"Estoque atualizado: {produto}")
    except ValueError as erro:
        print(f"Erro: {erro}")


def remover_produto(estoque):
    id_produto = ler_inteiro("ID do produto a remover: ")
    try:
        produto = estoque.remover_produto(id_produto)
        print(f"Produto removido: {produto}")
    except ValueError as erro:
        print(f"Erro: {erro}")


def listar_produtos_ordem_inversa(estoque):
    produtos = estoque.listar_produtos_fim_inicio()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for produto in produtos:
        print(produto)


def listar_produtos_ordenados(estoque):
    produtos = estoque.produtos_ordenados_por_id()
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for produto in produtos:
        print(produto)


def buscar_produto_binaria(estoque):
    id_produto = ler_inteiro("ID do produto: ")
    produto = estoque.buscar_produto_binaria(id_produto)
    print(produto if produto else "Produto não encontrado.")


def realizar_venda(estoque):
    id_cliente = ler_inteiro("ID do cliente: ")
    itens = []
    print("Informe os produtos da venda (ID do produto -1 para finalizar):")
    while True:
        id_produto = ler_inteiro("  ID do produto (-1 para finalizar): ")
        if id_produto == -1:
            break
        quantidade = ler_inteiro("  Quantidade: ")
        itens.append((id_produto, quantidade))
    try:
        venda = estoque.realizar_venda(id_cliente, itens)
        print("Venda realizada com sucesso!")
        print(venda)
    except ValueError as erro:
        print(f"Erro: {erro}")


def visualizar_fila_vendas(estoque):
    vendas = estoque.visualizar_fila_vendas()
    if not vendas:
        print("Nenhuma venda registrada.")
        return
    for venda in vendas:
        print(venda)


def visualizar_primeira_venda(estoque):
    venda = estoque.ver_primeira_venda()
    print(venda if venda else "A fila de vendas está vazia.")


def exibir_valor_total_estoque(estoque):
    print(f"Valor total do estoque: R$ {estoque.valor_total_estoque():.2f}")


def exibir_valor_total_vendas(estoque):
    print(f"Valor total das vendas: R$ {estoque.valor_total_vendas():.2f}")


def exibir_clientes_valores_gastos(estoque):
    totais = estoque.clientes_e_valores_gastos()
    if not totais:
        print("Nenhuma venda registrada ainda.")
        return
    for id_cliente, nome, total in totais:
        print(f"[{id_cliente}] {nome} - Total gasto: R$ {total:.2f}")


def exibir_cliente_que_mais_gastou(estoque):
    resultado = estoque.cliente_que_mais_gastou()
    if resultado is None:
        print("Nenhuma venda registrada ainda.")
        return
    id_cliente, nome, total = resultado
    print(f"Cliente que mais gastou: [{id_cliente}] {nome} - R$ {total:.2f}")


def exibir_produto_mais_vendido(estoque):
    resultado = estoque.produto_mais_vendido()
    if resultado is None:
        print("Nenhuma venda registrada ainda.")
        return
    id_produto, nome, quantidade = resultado
    print(f"Produto mais vendido: [{id_produto}] {nome} - {quantidade} unidades")


def desfazer_ultima_operacao(estoque):
    try:
        operacao = estoque.desfazer_ultima_operacao()
        print(f"Operação desfeita: {operacao['tipo']}")
    except ValueError as erro:
        print(f"Erro: {erro}")


ACOES = {
    1: cadastrar_cliente,
    2: listar_clientes,
    3: buscar_cliente,
    4: remover_cliente,
    5: cadastrar_produto,
    6: listar_produtos,
    7: buscar_produto,
    8: atualizar_estoque,
    9: remover_produto,
    10: listar_produtos_ordem_inversa,
    11: listar_produtos_ordenados,
    12: buscar_produto_binaria,
    13: realizar_venda,
    14: visualizar_fila_vendas,
    15: visualizar_primeira_venda,
    16: exibir_valor_total_estoque,
    17: exibir_valor_total_vendas,
    18: exibir_clientes_valores_gastos,
    19: exibir_cliente_que_mais_gastou,
    20: exibir_produto_mais_vendido,
    21: desfazer_ultima_operacao,
}


def main():
    estoque = Estoque()
    while True:
        exibir_menu()
        opcao = ler_opcao_menu()

        if opcao == 0:
            print("Encerrando o sistema. Até logo!")
            break

        acao = ACOES.get(opcao)
        if acao is None:
            print("Opção inválida. Tente novamente.")
            continue

        try:
            acao(estoque)
        except Exception as erro:  
            print(f"Ocorreu um erro inesperado, mas o sistema continua: {erro}")


if __name__ == "__main__":
    main()
