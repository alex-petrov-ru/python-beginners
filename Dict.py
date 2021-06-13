# N - количество бюллитений
votes = {}
N = int(input())
for i in range(N):
    name = input()
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1

A = list(votes.items())
print(A)

# D[name] = D.pop(name,0) + 1