import turtle
import math
turtle.shape("turtle")


def poly(rad, num):
    len = 2*rad*math.sin(math.pi/num)
    ang = 180*(1-2/num)
    turtle.left(180-ang/2)


    for j in range(num):
        turtle.forward(len)
        turtle.left(180-ang)

rad = 30
num = 3


for i in range(10):
    poly(rad, num)
    ang = 180*(1-2/num)

    turtle.right(180-ang/2)
    turtle.penup()
    turtle.forward(20)
    turtle.down()

    num += 1
    rad += 20