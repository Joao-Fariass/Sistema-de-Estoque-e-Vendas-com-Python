class ItemVenda:
    def __init__(self, produto_id, quantidade, preco_unitario):
        self.produto_id = produto_id
        self.quantidade = quantidade
        self.preco_unitario = preco_unitario

    def subtotal(self):
        return self.quantidade * self.preco_unitario

    def codificar(self):
        return f"{self.produto_id}:{self.quantidade}:{self.preco_unitario}"

    @staticmethod
    def decodificar(texto):
        pid, qtd, preco = texto.split(":")
        return ItemVenda(int(pid), int(qtd), float(preco))


class Venda:
    def __init__(self, id_venda, cliente_id, itens):
        self.id = id_venda
        self.cliente_id = cliente_id
        self.itens = itens  # lista de ItemVenda
        self.valor_total = sum(item.subtotal() for item in itens)

    def __str__(self):
        linhas = [f"Venda [{self.id}] - Cliente ID {self.cliente_id} - "
                  f"Total: R$ {self.valor_total:.2f}"]
        for item in self.itens:
            linhas.append(f"    Produto {item.produto_id} x{item.quantidade} "
                           f"= R$ {item.subtotal():.2f}")
        return "\n".join(linhas)

    def to_csv_row(self):
        itens_codificados = "|".join(item.codificar() for item in self.itens)
        return [str(self.id), str(self.cliente_id), itens_codificados,
                str(self.valor_total)]

    @staticmethod
    def from_csv_row(row):
        id_venda = int(row[0])
        cliente_id = int(row[1])
        itens_texto = row[2]
        itens = [ItemVenda.decodificar(t) for t in itens_texto.split("|") if t]
        return Venda(id_venda, cliente_id, itens)
