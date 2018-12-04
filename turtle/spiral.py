import turtle
import math
turtle.shape("turtle")


rad = 5
num = 50

for i in range(10):
    x = 50/num
    for j in range(num):
        len = 2*rad*math.sin(math.pi/num)
        ang = 180*(1-2/num)
        turtle.forward(len)
        turtle.left(180-ang)
        rad += x