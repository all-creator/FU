from time import sleep
from math import sin, cos, pi
from tkinter import *


def c(p):
    return p + (r_w / 2)


def sgn(x_sng):
    return ((x_sng > 0) - (x_sng < 0)) * 1


def update():
    global pol, canvas
    canvas.delete(ALL)
    create()


def create():
    global pol, canvas
    t = 0
    for _ in range(step + 1):
        x = (abs((cos(t))) ** na) * a * sgn(cos(t)) #нахождение х элипса
        y = (abs((sin(t))) ** na) * b * sgn(sin(t)) #нахождение у элипса

        dots.append(int(c(x)))
        dots.append(int(c(y)))

        t += piece
    pol = canvas.create_polygon(dots)


def resize(event):
    global n, na
    if event.type == EventType.Motion:
        if 550 > event.y > 500 and 550 > event.x > 50:
            update()
            n = (event.x - 50) / 5
            n = round(5 / 100 * n, 2)
            na = 2 / n
            s = "N = {}".format(n)
            root.title(s)
            update()
    else:
        update()
        n += 0.5 #изменение угла эллипса
        if n > 4.9:
            n = 0.1
        na = 2 / n
        s = "N = {}".format(n)
        root.title(s)
        update()


r_w = 600 #размер canvas
root = Tk()
canvas = Canvas(root, width=r_w, height=r_w, bg="white")
canvas.pack()
canvas.bind('<Motion>', resize)
canvas.bind('<Button-1>', resize)

dots = []

a, b, n = 200, 200, 0.1 #начальные переменные
na = 2 / n
step = 100
piece = (pi * 2) / step
pol = canvas.create_polygon(0, 0)

update()

root.mainloop()
