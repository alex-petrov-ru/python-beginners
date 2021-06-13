limit = int(input())
a = [0,0,1]
for _ in range(limit-3):
    a.append(sum(a[-3:]))
for k in range(len(a)):
    if a[k] <= limit < a[k+1]:
        print(k+1)

