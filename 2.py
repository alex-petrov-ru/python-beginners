"""
По заданной квадратной матрице n×n из нулей и единиц определите,
может ли данная матрица быть матрицей смежности простого неориентированного графа.
"""

# n = int(input())
# answer = "YES"
# g = [[0] * n for _ in range(n)]
# for i in range(n):
#     lst = list(map(int, input().split()))
#     for j in range(n):
#         g[i][j] = lst[j]
#
# for i in range(n):
#     for j in range(n):
#         if g[i][j] != g[j][i]:
#             answer = "NO"
#         if g[i][i] != 0:
#             answer = "NO"

# print(answer)

a = int(input())
b = int(input())
s = a + b
print(s)