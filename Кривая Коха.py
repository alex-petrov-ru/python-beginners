import turtle

def koha(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        x = l // 3
        koha(x, n-1)
        turtle.left(60)
        koha(x, n-1)
        turtle.right(120)
        koha(x, n-1)
        turtle.left(60)
        koha(x, n-1)

koha(300,1)
turtle.speed('fastest')

