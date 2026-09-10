from estruturas.nodo import NodoDuplo


class ListaDuplamenteEncadeada:
    

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def inserir(self, dado):
        novo = NodoDuplo(dado)
        if self.inicio is None:
            self.inicio = novo
            self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo
        self.tamanho += 1

    def buscar(self, id_procurado):
        atual = self.inicio
        while atual is not None:
            if atual.dado.id == id_procurado:
                return atual.dado
            atual = atual.proximo
        return None

    def existe_id(self, id_procurado):
        return self.buscar(id_procurado) is not None

    def remover(self, id_procurado):
        atual = self.inicio
        while atual is not None:
            if atual.dado.id == id_procurado:
                if atual.anterior is not None:
                    atual.anterior.proximo = atual.proximo
                else:
                    self.inicio = atual.proximo
                if atual.proximo is not None:
                    atual.proximo.anterior = atual.anterior
                else:
                    self.fim = atual.anterior
                self.tamanho -= 1
                return atual.dado
            atual = atual.proximo
        return None

    def listar_inicio_fim(self):
        resultado = []
        atual = self.inicio
        while atual is not None:
            resultado.append(atual.dado)
            atual = atual.proximo
        return resultado

    def listar_fim_inicio(self):
        resultado = []
        atual = self.fim
        while atual is not None:
            resultado.append(atual.dado)
            atual = atual.anterior
        return resultado

    def para_lista_auxiliar(self):
        
        return self.listar_inicio_fim()

    def __iter__(self):
        atual = self.inicio
        while atual is not None:
            yield atual.dado
            atual = atual.proximo

    def __len__(self):
        return self.tamanho
    