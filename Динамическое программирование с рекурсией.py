F = [None] * 10000
def fib(n:int) -> int:
    assert (n >= 0 and n < 10000)
    if F[n] is not None:
        return F[n]
    elif n <= 1:
        F[n] = n
        return F[n]
    else:
        F[n] = fib(n-1) + fib(n-2)
        return F[n]


print(fib(994))