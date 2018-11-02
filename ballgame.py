

from tkinter import *
import random
from random import randint
import time

root = Tk()
root.geometry('800x600')
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

spectrum =['red', 'orange', 'yellow', 'green', 'blue', 'purple']

def appear():
    canv.after(1000, appear)
    global r
    x = randint(15, 750)
    y = randint(15, 550)
    r = randint(15, 60)
    canv.create_oval(x-r, y-r, x+r, y+r, fill=random.choice(spectrum), outline=random.choice(spectrum))



appear()


mainloop()