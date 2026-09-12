class Cliente:
    def __init__(self, id_cliente, nome):
        self.id = id_cliente
        self.nome = nome

    def __str__(self):
        return f"[{self.id}] {self.nome}"

    def to_csv_row(self):
        return [str(self.id), self.nome]

    @staticmethod
    def from_csv_row(row):
        return Cliente(int(row[0]), row[1])