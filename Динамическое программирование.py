# Кузнечик
# Запретим некоторые клетки для посещения

def count_trajectories(n, allowed: list):
    K = [0, 1, int(allowed[2])] + [0]*(n-2)
    for i in range(3, n+1):
        if allowed[i]:
            K[i] = K[i-1] + K[i-2] - K[i-3]
    return K[n]
