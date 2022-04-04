import math
from tkinter import *
from threading import Thread
from time import sleep


class Obj:
    def __init__(self, item, weight, x, y):
        self.weight = weight
        self.item = item
        self.x = x
        self.y = y

    def move(self, x, y):
        c.move(self.item, x, y)
        self.x += x
        self.y += y


root = Tk()
c = Canvas(root, width=600, height=600, bg="white")
c.pack()


er = Obj(c.create_oval(300, 100, 320, 120), 100, 310, 110)
ar = Obj(c.create_oval(200, 100, 210, 110), 50, 205, 105)


def life():
    while True:
        x = math.ceil((ar.weight * er.weight) / (ar.x - er.x) ** 2)
        print(x)
        if er.x - ar.x > 0:
            ar.move(x, 0)
        elif er.x - ar.x < 0:
            ar.move(-x, 0)
        else:
            ar.move(0, 0)
        sleep(0.1)


live = Thread(target=life)
live.start()

root.mainloop()

