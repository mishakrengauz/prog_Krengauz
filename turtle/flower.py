import turtle
import math
turtle.shape("turtle")


rad = 50
num = 100
partsnum = 3
len = 2*rad*math.sin(math.pi/num)
ang = 180*(1-2/num)


def circle(sign):
    for i in range(num):
        turtle.forward(len)
        turtle.left(sign*(180-ang))


turtle.speed('fastest')

for i in range(partsnum):
    circle(-1)
    circle(1)
    turtle.left(180/partsnum)