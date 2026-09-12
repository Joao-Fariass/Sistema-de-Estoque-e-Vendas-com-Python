
Disciplina: ORGANIZAÇÃO E ABSTRAÇÃO NA PROGRAMAÇÃO.


Trabalho: Sistema de estoque e vendas. 



Integrantes:
Arthur Saggin RA: 1139361

André Alves Neto RA: 1139890

Cassio Soder RA: 1139496

Lucas Varal RA: 1136676

João Isaque RA: 1139559

Nycolas Jungbeck RA: 1139527




Descrição e execução
Sistema de loja rodado no terminal: cadastra clientes/produtos, controla estoque, registra vendas, desfaz a última operação e busca produtos. Executa com python main.py, sem dependências externas.




Estrutura de diretórios
main.py (menu) → services/ (regras de negócio + persistência) → estruturas/ (LSE, LDE, Fila, Pilha) → models/ (Cliente, Produto, Venda) → algoritmos/ (ordenação e busca) → data/ (CSVs).




LSE, LDE, Fila e Pilha
LSE: guarda os clientes (cada nodo aponta só pro próximo).
LDE: guarda os produtos (cada nodo aponta pros dois lados, permite listar do início ao fim e vice-versa).
Fila: guarda as vendas na ordem em que aconteceram (FIFO — primeira venda registrada é a primeira da fila).
Pilha: guarda o histórico de operações (LIFO — cada ação empilha um registro; desfazer sempre reverte a mais recente).




Algoritmo de ordenação, Busca Binária e persistência
Ordenação: Insertion Sort feito na mão (sem sort()), ordena produtos por ID.
Busca Binária: feita na mão, sempre sobre a lista já ordenada, corta o intervalo pela metade a cada tentativa.
Persistência: salva/carrega sozinho em clientes.csv, produtos.csv, vendas.csv — sem opção manual de salvar.



Complexidade
Insertion Sort: no pior caso e no caso médio, o tempo de execução cresce proporcionalmente ao quadrado da quantidade de produtos — ou seja, dobrar a lista de produtos deixa a ordenação bem mais lenta, não só o dobro. No melhor caso, quando os produtos já estão praticamente ordenados, ele é rápido, crescendo de forma proporcional (linear) à quantidade de itens.
Busca Binária: é bem mais eficiente — o tempo cresce muito devagar mesmo com listas grandes, porque a cada tentativa ela descarta metade dos produtos restantes. Não precisa de espaço extra de memória além de algumas variáveis de controle, já que não usa recursão.
