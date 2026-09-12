from estruturas.nodo import NodoSimples


class ListaSimplesmenteEncadeada:
    
    def __init__(self):
        self.inicio = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def inserir(self, dado):
        novo = NodoSimples(dado)
        if self.inicio is None:
            self.inicio = novo
        else:
            atual = self.inicio
            while atual.proximo is not None:
                atual = atual.proximo
            atual.proximo = novo
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
        anterior = None
        atual = self.inicio
        while atual is not None:
            if atual.dado.id == id_procurado:
                if anterior is None:
                    self.inicio = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.tamanho -= 1
                return atual.dado
            anterior = atual
            atual = atual.proximo
        return None

    def inserir_dado_bruto(self, dado):
        
        self.inserir(dado)

    def listar(self):
        resultado = []
        atual = self.inicio
        while atual is not None:
            resultado.append(atual.dado)
            atual = atual.proximo
        return resultado

    def _iter_(self):
        atual = self.inicio
        while atual is not None:
            yield atual.dado
            atual = atual.proximo

    def _len_(self):
        return self.tamanho