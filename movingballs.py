from tkinter import *

root = Tk()
root.geometry("300x300")
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)

balls = []

for x, y, dx, dy in (100, 100, 2, 3), (200, 200, -2, 3), (200, 200, -3, 3), (200, 100, -2, 3), (200, 100, 2, 3):
    oval = canvas.create_oval(x, y, x+40, y+40, fill='blue')
    ball = [x, y, dx, dy, oval]
    balls.append(ball)

def tick_handler():
    for ball in balls:
        x, y, dx, dy, oval = ball
        if x < 0:
            dx = -dx; x = 0
        elif x > 300-40:
            dx = -dx
            x = 300-40
        if y < 0:
            dy = -dy
            y = 0
        elif y > 300-40:
            dy = -dy
            y = 300-40
        x = x + dx; y = y + dy
        canvas.move(oval, dx, dy)
        ball[0] = x
        ball[1] = y
        ball[2] = dx
        ball[3] = dy


def time_handler():
    global freeze
    speed = speed_scale.get()
    if speed == 0:
        print("Заморозка!")
        freeze = True
        return
    tick_handler()
    sleep_dt = 1100 - 100*speed
    root.after(sleep_dt, time_handler)

def unfreezer(event):
    global freeze
    if freeze == True:
        speed = speed_scale.get()
        if speed != 0:
            freeze = False
            root.after(0, time_handler)

speed_scale = Scale(root, orient=HORIZONTAL, length=300,
               from_=0, to=10, tickinterval=1, resolution=1)
speed_scale.pack()

speed_scale.set(1);
freeze = False

root.after(10, time_handler)
speed_scale.bind("<Motion>", unfreezer)
root.mainloop()
