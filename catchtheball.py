from tkinter import *
import random
from random import randint
from tkinter import Label

root = Tk()
root.geometry('800x600')
root.title("Catch it")
canv = Canvas(root, bg='white')
canv.pack(fill=BOTH, expand=1)

spectrum = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
existFlags = {}

catched = 0
missed = 0

scoreboard = Label(root,
                   text="Число пойманных шаров : {}".format(catched) + " Число упущенных шаров: {}".format(missed))
scoreboard.pack(anchor='n')


def updatescoreboard():
    scoreboard['text'] = "Число пойманных шаров : {}".format(catched) + " Число упущенных шаров: {}".format(missed)


def onobjectclick(event, arg):
    global catched
    global missed
    canv.delete(arg)
    catched = catched + 1
    existFlags[arg] = 0
    updatescoreboard()


def deleteCircle(arg):
    global catched
    global missed
    if existFlags[arg] == 1:
        canv.delete(arg)
        missed = missed + 1
        updatescoreboard()


def appear():
    canv.after(1000, appear)
    global r
    x = randint(15, 750)
    y = randint(15, 550)
    r = randint(15, 60)
    objid = canv.create_oval(x - r, y - r, x + r, y + r, fill=random.choice(spectrum), outline=random.choice(spectrum))
    canv.tag_bind(objid, '<ButtonPress-1>', lambda event, arg=objid: onobjectclick(event, arg))
    existFlags[objid] = 1  
    root.after(2000, deleteCircle, objid)


appear()

mainloop()
