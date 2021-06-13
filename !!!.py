def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    pass

def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
    pass

def pow(a: float, n: int):
    if n == 0:
        return 1
    elif n%2 == 1: #нечётный
        return pow(a, n-1)*a
    else: #чётный
        return pow(a**2, n//2)
    pass

def
