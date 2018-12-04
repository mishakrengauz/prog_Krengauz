import turtle
import math
turtle.shape("turtle")


def arc(rad, num):
    len = 2*rad*math.sin(math.pi/num/2)
    turtle.right(90/num)
    for i in range(num):
        turtle.forward(len)
        turtle.right(180/num)

    turtle.left(90/n)

R = 70
r = 10
N = 20
n = 10
parts = 2

turtle.left(90)

for i in range(parts):
    arc(R, N)
    arc(r, n)

