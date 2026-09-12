from estruturas.nodo import NodoSimples


class Fila:

    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def esta_vazia(self):
        return self.inicio is None

    def enfileirar(self, dado):
        novo = NodoSimples(dado)
        if self.fim is None:
            self.inicio = novo
            self.fim = novo
        else:
            self.fim.proximo = novo
            self.fim = novo
        self.tamanho += 1

    def desenfileirar(self):
        if self.inicio is None:
            return None
        dado = self.inicio.dado
        self.inicio = self.inicio.proximo
        if self.inicio is None:
            self.fim = None
        self.tamanho -= 1
        return dado

    def remover_ultimo(self):
        if self.inicio is None:
            return None
        if self.inicio is self.fim:
            dado = self.inicio.dado
            self.inicio = None
            self.fim = None
            self.tamanho -= 1
            return dado
        atual = self.inicio
        while atual.proximo is not self.fim:
            atual = atual.proximo
        dado = self.fim.dado
        atual.proximo = None
        self.fim = atual
        self.tamanho -= 1
        return dado

    def ver_primeiro(self):
        if self.inicio is None:
            return None
        return self.inicio.dado

    def listar(self):
        resultado = []
        atual = self.inicio
        while atual is not None:
            resultado.append(atual.dado)
            atual = atual.proximo
        return resultado

    def __iter__(self):
        atual = self.inicio
        while atual is not None:
            yield atual.dado
            atual = atual.proximo

    def __len__(self):
        return self.tamanho
