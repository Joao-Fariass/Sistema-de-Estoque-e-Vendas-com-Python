def ler_opcao_menu():
    texto = input("Escolha uma opção: ").strip()
    try:
        return int(texto)
    except ValueError:
        return -1  # opção inválida, tratada no loop principal


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


def main():
    # TODO: integrar com services/estoque_service.py quando estiver pronto
    while True:
        exibir_menu()
        opcao = ler_opcao_menu()

        if opcao == 0:
            print("Encerrando o sistema. Até logo!")
            break

        if opcao < 0 or opcao > 21:
            print("Opção inválida. Tente novamente.")
            continue

        print("Funcionalidade ainda não implementada.")


if __name__ == "__main__":
    main()