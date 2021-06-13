N = int(input())
a = [0] * N
for i in range(N):
    a[i] = int(input())

num = a[0]
max_frq = 1
for i in range(N - 1):
    frq = 1
    for k in range(i + 1, N):
        if a[i] == a[k]:
            frq += 1
    if frq > max_frq:
        max_frq = frq
        num = a[i]

if max_frq > 1:
    print(num)
