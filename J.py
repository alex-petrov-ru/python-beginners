# Генерация всех перестановок
# M - длина числа
# N - основание системы счисления
def gen_bin(M, prefix=""):
    if M == 0:
        print(prefix)
    for digit in "0", "1":
        gen_bin(M-1, prefix+digit)
                                     # gen_bin(M - 1, prefix + "0")
                                     # gen_bin(M - 1, prefix + "1")



def generate_numbers(N:int, M:int, prefix=None):
    """ Генерирует все числа (с лидирующими незначащими нулями)
        в N-ричной системе счисления (n <= 10)
        длины M
    """
    prefix = prefix or []
    if M == 0:
        print(prefix)
        return
    for digit in range(N):
        prefix.append(digit)
        generate_numbers(N, M-1, prefix)
        prefix.pop()
# только для двоичной системы счисления
# gen_bin(5)
# для произвольной СС
generate_numbers(3, 3)