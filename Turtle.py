import turtle

turtle.shape('turtle')


l = 400
n = int(input())

turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()


def koch(l, n):
    if n == 0:
        turtle.forward(l)
        return

    a = l / 3
    koch(a, n - 1)
    turtle.left(60)
    koch(a, n - 1)
    turtle.right(120)
    koch(a, n - 1)
    turtle.left(60)
    koch(a, n - 1)


def loop():
    koch(l, n)
    turtle.right(120)
    koch(l, n)
    turtle.right(120)
    koch(l, n)


loop()