from tkinter import *
import random
from random import randint
from tkinter import Label


def updatescoreboard(scoreboard):
    scoreboard['text'] = "Число пойманных шаров : {}".format(catched) + " Число упущенных шаров: {}".format(missed)


def onobjectclick(arg, canv, existFlags, scoreboard):
    global catched
    global missed
    canv.delete(arg)
    catched = catched + 1
    existFlags[arg] = 0
    updatescoreboard(scoreboard)


def deleteCircle(arg, canv, existFlags, scoreboard):
    global catched
    global missed
    if existFlags[arg] == 1:
        canv.delete(arg)
        missed = missed + 1
        updatescoreboard(scoreboard)


def appear(canv, spectrum, existFlags, root, scoreboard):
    canv.after(1000, appear, canv, spectrum, scoreboard, root, existFlags)
    global r
    x = randint(15, 750)
    y = randint(15, 550)
    r = randint(15, 60)
    objid = canv.create_oval(x - r, y - r, x + r, y + r, fill=random.choice(spectrum),
                                                     outline=random.choice(spectrum))
    canv.tag_bind(objid, '<ButtonPress-1>', lambda event, arg=objid: onobjectclick(arg, canv, existFlags, scoreboard))
    existFlags[objid] = 1
    root.after(1000, deleteCircle, objid, canv, existFlags, scoreboard)


def main():
    root = Tk()
    root.geometry('800x600')
    root.title("Catch it")
    canv = Canvas(root, bg='white')
    canv.pack(fill=BOTH, expand=1)
    spectrum = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    existFlags = {}
    global catched
    global missed
    catched = 0
    missed = 0
    scoreboard = Label(root,
                       text="Число пойманных шаров : {}".format(catched) + " Число упущенных шаров: {}".format(missed))
    scoreboard.pack(anchor='n')
    appear(canv, spectrum, existFlags, root, scoreboard)


if __name__ == "__main__":
    main()


mainloop()
