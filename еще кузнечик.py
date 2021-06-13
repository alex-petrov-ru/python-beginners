# price[i] - за посещение клетки i
# C[i] - cost, минимальная стоимость достижения клетки i

def count_min_cost(n, price: list):
    C = [None, price[1], price[2]] + [0]*(n-2)
    for i in range(3, n+1):
        C[i] = price[i] + min(C[i-1], C[i-2])
    return C[n]