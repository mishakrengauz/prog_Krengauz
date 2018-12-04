import turtle
import math
turtle.shape("turtle")


rad = 50
num = 100
partsnum = 5
len = 2*rad*math.sin(math.pi/num)
ang = 180*(1-2/num)


def circle(sign):
   
    len = 2 * rad * math.sin(math.pi / num)
    ang = 180 * (1 - 2 / num)
    for i in range(num):
        turtle.left(sign * (180 - ang))
        turtle.forward(len)


turtle.speed('fastest')

turtle.left(90)

for i in range(partsnum):
    circle(-1)
    circle(1)
    rad+=10