A = []
x = 0
i = 0
k = int(input())
A.append(k)
while k != 0:
    k = int(input())
    A.append(k)
    if i > 5:
        A.pop(0)
    if A[0] > x:
        x = A[0]
    i += 1
print (x)