a = [int(i) for i in input().split()]
k = 1
n = 0
for i in range(len(a)):
    for k in range(k, len(a)):
        if a[i] == a[k]:
            n += 1
print(n)
