def dfs(vertex, G, used):
    used.add(vertex)
    for neighbor in G[vertex]:
        if neighbor not in used:
            dfs(neighbor, G, used)


used = set()
N = 0
for vertex in G:
    if vertex not in used:
        dfs(vertex, G, used)
        N += 1
print(N)

