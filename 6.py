def king(n, m):
    F = [[0] * (m+1) for i in range(n+1)]
    for i in range(n):
        F[i][0] = 1
    for j in range(m):
        F[0][j] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            F[i][j] = F[i-1][j] + F[i][j-1] + F[-1][j-1]
    return F[n][m]


print(king(124, 19))


