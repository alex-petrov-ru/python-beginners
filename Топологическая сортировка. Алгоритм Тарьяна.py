visited = [False] * (n + 1)
ans = []


def dfs(start, G, visited, ans):
    visited[start] = True
    for u in G[start]:
        if not visited[u]:
            dfs(u, G, visited, ans)
    ans.append(start)


for i in range(1, n + 1):
    if not visited[i]:
        dfs(i, G, visited, ans)


ans[:] = ans[::-1  ]