import turtle
import math

def star(rad, num):
    a = 2*rad*math.sin(math.pi/num)
    len = a/(2*(1-math.cos(math.pi/num)))*0.2

    for i in range(num):
        turtle.forward(len)
        turtle.left(180-180/num)

number = 5

star(100, number)