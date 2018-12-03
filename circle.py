import turtle
import math
turtle.shape("turtle")

rad = 100
num = 100
len = 2*rad*math.sin(math.pi/num)
ang = 180*(1-2/num)

for i in range(num):
    turtle.forward(len)
    turtle.left(180-ang)