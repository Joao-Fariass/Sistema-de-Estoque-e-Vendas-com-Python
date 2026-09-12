def insertion_sort(lista, chave=lambda x: x.id, crescente=True):
    """
    Ordena uma lista com o algoritmo Insertion Sort, implementado manualmente
    (sem usar sort() ou sorted()).

    lista: lista de objetos a ordenar (não é alterada, uma cópia é retornada)
    chave: função que extrai o valor usado na comparação
    crescente: True para ordem crescente, False para decrescente

    Complexidade: O(n^2) no pior e médio caso, O(n) no melhor caso
    (lista já ordenada). Espaço extra O(n) por causa da cópia.
    """
    dados = list(lista)  
    for i in range(1, len(dados)):
        atual = dados[i]
        valor_atual = chave(atual)
        j = i - 1
        while j >= 0 and (
            (crescente and chave(dados[j]) > valor_atual)
            or (not crescente and chave(dados[j]) < valor_atual)
        ):
            dados[j + 1] = dados[j]
            j -= 1
        dados[j + 1] = atual
    return dados
