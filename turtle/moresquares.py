
import turtle
turtle.shape("turtle")

len = 10
for i in range(10):
    turtle.penup()
    turtle.goto(-len/2, -len/2)
    turtle.pendown()
    for k in range(4):
        turtle.forward(len)
        turtle.left(90)
    len += 40