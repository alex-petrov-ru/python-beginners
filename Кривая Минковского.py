import turtle

def minkov(l,n):
    if n == 0:
        turtle.forward(l)
    else:
        x = l // 4
        minkov(x, n-1)
        turtle.left(90)
        minkov(x, n - 1)
        turtle.right(90)
        minkov(x, n - 1)
        turtle.right(90)
        minkov(2*x, n - 1)
        turtle.left(90)
        minkov(x, n - 1)
        turtle.left(90)
        minkov(x, n - 1)
        turtle.right(90)
        minkov(x, n - 1)

minkov(200,2)