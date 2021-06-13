def trenirovka(a, b):
    if a > b:
        if a == b:
            return print(b)
        else:
            print(a)
            trenirovka(a-1, b)
    else:
        if b == a:
            return print(a)
        else:
            print(b)
            trenirovka(a, b-1)


trenirovka(2, 10)