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

def snowflake(l,n):
    for i in range(3):
        koha(l, n)
        turtle.right(120)

snowflake(300,4)
turtle.speed('fastest')