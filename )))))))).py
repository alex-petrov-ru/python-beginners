"""
A = [True, 2, 5.3, "hello"]
for x in A:
    print(type(x))

B = [True, 2, 5.3, A]
for x in B:
    print(type(A))

"""

C = [(1, 5), (-3, 4), (-7, 2), (8, 3), (0, 0)]
for x,y in C:
    print(x,y)