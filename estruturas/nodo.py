class NodoSimples:
    

    def _init_(self, dado):
        self.dado = dado
        self.proximo = None


class NodoDuplo:
    
    def _init_(self, dado):
        self.dado = dado
        self.proximo = None
        self.anterior = None