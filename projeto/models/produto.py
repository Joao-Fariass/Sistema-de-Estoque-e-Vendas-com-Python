class Produto:
    def __init__(self, id_produto, nome, quantidade, preco):
        self.id = id_produto
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return (f"[{self.id}] {self.nome} - Qtd: {self.quantidade} - "
                f"Preço: R$ {self.preco:.2f}")

    def to_csv_row(self):
        return [str(self.id), self.nome, str(self.quantidade), str(self.preco)]

    @staticmethod
    def from_csv_row(row):
        return Produto(int(row[0]), row[1], int(row[2]), float(row[3]))