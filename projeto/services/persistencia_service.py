import csv
import os

from models.cliente import Cliente
from models.produto import Produto
from models.venda import Venda


class PersistenciaService:
    def __init__(self, pasta_data="data"):
        self.pasta_data = pasta_data
        os.makedirs(self.pasta_data, exist_ok=True)
        self.caminho_clientes = os.path.join(pasta_data, "clientes.csv")
        self.caminho_produtos = os.path.join(pasta_data, "produtos.csv")
        self.caminho_vendas = os.path.join(pasta_data, "vendas.csv")

    def _ler_csv(self, caminho, cabecalho):
        linhas = []
        if not os.path.exists(caminho):
            return linhas
        try:
            with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
                leitor = csv.reader(arquivo)
                primeira = True
                for row in leitor:
                    if not row:
                        continue
                    if primeira and row == cabecalho:
                        primeira = False
                        continue
                    primeira = False
                    linhas.append(row)
        except (OSError, csv.Error):
           
            return []
        return linhas

    def _escrever_csv(self, caminho, cabecalho, linhas):
        try:
            with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(cabecalho)
                for linha in linhas:
                    escritor.writerow(linha)
        except OSError as erro:
            print(f"Aviso: não foi possível salvar em {caminho} ({erro}).")

    
    def carregar_clientes(self):
        clientes = []
        for row in self._ler_csv(self.caminho_clientes, ["id", "nome"]):
            try:
                clientes.append(Cliente.from_csv_row(row))
            except (ValueError, IndexError):
                continue  
        return clientes

    def salvar_clientes(self, lista_clientes):
        linhas = [c.to_csv_row() for c in lista_clientes]
        self._escrever_csv(self.caminho_clientes, ["id", "nome"], linhas)

   
    def carregar_produtos(self):
        produtos = []
        cabecalho = ["id", "nome", "quantidade", "preco"]
        for row in self._ler_csv(self.caminho_produtos, cabecalho):
            try:
                produtos.append(Produto.from_csv_row(row))
            except (ValueError, IndexError):
                continue
        return produtos

    def salvar_produtos(self, lista_produtos):
        cabecalho = ["id", "nome", "quantidade", "preco"]
        linhas = [p.to_csv_row() for p in lista_produtos]
        self._escrever_csv(self.caminho_produtos, cabecalho, linhas)

    
    def carregar_vendas(self):
        vendas = []
        cabecalho = ["id", "cliente_id", "itens", "valor_total"]
        for row in self._ler_csv(self.caminho_vendas, cabecalho):
            try:
                vendas.append(Venda.from_csv_row(row))
            except (ValueError, IndexError):
                continue
        return vendas

    def salvar_vendas(self, lista_vendas):
        cabecalho = ["id", "cliente_id", "itens", "valor_total"]
        linhas = [v.to_csv_row() for v in lista_vendas]
        self._escrever_csv(self.caminho_vendas, cabecalho, linhas)