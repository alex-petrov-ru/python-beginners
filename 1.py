""" Простой неориентированный граф задан матрицей смежности.
    Найдите количество ребер в графе.
"""

m = (map(int, input().split()) for _ in range(int(input('Num of nodes: '))))
a = {frozenset([ci+1, ni+1]) for ni, ne in enumerate(m) for ci, ce in enumerate(ne) if ce == 1}
print('Num of edges:', len(a))

m = (map(int, input().split()) for _ in range(int(input())))
a =