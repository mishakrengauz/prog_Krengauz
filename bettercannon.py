from tkinter import *
from random import randrange as rnd, choice
import math


import time

root = Tk()
fr = Frame(root)
root.geometry('800x600')
canv = Canvas(root, bg='cyan')
canv.pack(fill=BOTH, expand=1)




class Ball:
    def __init__(self, x=40, y=450):
        self.x = x
        self.y = y
        self.r = 1
        self.vx = 0
        self.vy = 0
        #self.color = 'black'
        self.circle = canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                                       fill = 'red')
        self.live = 30

    def coord(self):
        canv.coords(self.circle, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)

    def move(self):
        if self.y <= 500:
            self.dy -= 1.2
            self.y -= self.dy
            self.x += self.dx
            self.dx *= 0.99
            self.coord()
        else:
            if self.dx**2+self.dy**2 > 10:
                self.dy = -self.dy/2
                self.dx = self.dx/2
                self.y = 499
            if self.live < 0:
                balls.pop(balls.index(self))
                canv.delete(self.circle)
            else:
                self.live -= 1
        if self.x > 780:
            self.dx = - self.dx/2
            self.x = 779

    def collision(self, ball):
        if abs(ball.x - self.x) <= (self.r + ball.r) and abs(ball.y - self.y) <= (self.r + ball.r):
            return True
        else:
            return False
        #a = abs(self.x + self.dx - ball.x)
        #b = abs(self.y + self.dy - ball.y)
        #return (a * a + b * b) ** 0.5 <= self.r + ball.r


class Gun:
    def __init__(self):
        self.power = 10
        self.on = 0
        self.angle = 1
        self.cannon = canv.create_line(20, 450, 50, 420, width=7)
        self.base = canv.create_line(20, 453, 20, 480, fill='brown', width=7)
        self.left_branch = canv.create_line(7, 430, 20, 450, fill='brown', width=7)
        self.right_branch = canv.create_line(33, 430, 20, 450, fill='brown', width=7)
        self.land = canv.create_rectangle(0, 480, 800, 600, fill='grey')

    def begin_shoot(self, event):
        self.on = 1

    def end_shoot(self, event):
        global balls, bullet
        bullet += 1
        new_ball = Ball()
        new_ball.r += 5
        self.angle = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))
        new_ball.dx = self.power * math.cos(self.angle)
        new_ball.dy = -self.power * math.sin(self.angle)
        balls.append(new_ball)
        self.on = 0
        self.power = 10

    def aiming(self, event=0):
        if event:
            self.angle = math.atan((event.y - 450) / (event.x - 20))

        canv.coords(self.cannon, 20, 450, 20 + max(self.power, 20) * math.cos(self.angle),
                    450 + max(self.power, 20) * math.sin(self.angle))

    def power_up(self):
        if self.on:
            if self.power < 100:
                self.power += 1



class target():
    def __init__(self):
        self.points = 0
        self.circle = canv.create_oval(0, 0, 0, 0)
        self.point = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()
        self.live = 1

    def new_target(self):
        x = self.x = rnd(600, 780)
        y = self.y = rnd(320, 450)
        r = self.r = rnd(20, 50)
        color = self.color = 'red'
        canv.coords(self.circle, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.circle, fill='green')

    def hit(self, points=1):
        canv.coords(self.circle, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.point, text=self.points)


tg = target()
screen = canv.create_text(400, 300, text='', font='28')
gn = Gun()
bullet = 0
balls = []


def new_game(event=''):
    global Gun, tg, screen, balls, bullet
    tg.new_target()
    bullet = 0
    balls = []
    canv.bind('<Button-1>', gn.begin_shoot)
    canv.bind('<ButtonRelease-1>', gn.end_shoot)
    canv.bind('<Motion>', gn.aiming
              )

    tg.live = 1
    while balls or tg.live:
        for bal in balls:
            bal.move()
            if bal.collision(tg) and tg.live:
                tg.live = 0
                tg.hit()
                canv.bind('<Button-1>', '')
                canv.bind('<ButtonRelease-1>', '')
                canv.itemconfig(screen, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
        canv.update()
        time.sleep(0.03)
        gn.aiming
        gn.power_up()
    canv.itemconfig(screen, text='')
    canv.delete(Gun)
    root.after(750, new_game)


new_game()

mainloop()
