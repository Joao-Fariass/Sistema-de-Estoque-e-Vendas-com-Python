def busca_binaria(lista_ordenada, id_procurado, chave=lambda x: x.id):
    inicio = 0
    fim = len(lista_ordenada) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        valor_meio = chave(lista_ordenada[meio])

        if valor_meio == id_procurado:
            return lista_ordenada[meio]
        elif valor_meio < id_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1

    return None