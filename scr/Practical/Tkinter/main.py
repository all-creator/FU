import math
from tkinter import *


class Dot:

    def __init__(self, x, y, diam, color):
        self.item = c.create_oval(x, y, x + diam, y + diam, fill=color)
        self.x = x
        self.y = y
        self.a = 0


root = Tk()
c = Canvas(root, width=600, height=600, bg="white")
c.grid(row=0, rowspan=10, column=0, columnspan=10)

ball = c.create_oval(100, 100, 500, 500, fill='black')

x0 = 280
y0 = 40
d = 40
t = 1
stop_p = False
dots = [Dot(x0, y0, d, 'black')]


def create():
    dots.append(Dot(x0, y0, d, 'black'))


def remove():
    rem_item = dots.pop().item
    c.delete(rem_item)


def motion():
    if stop_p:
        return
    global d, t
    for dot in dots:
        dot.a += 0.1
        if dot.a >= 360:
            dot.a = 0
        dot.x = (300 - d / 2) + (200 + d) * math.cos(dot.a * t)
        dot.y = (300 - d / 2) + (200 + d) * math.sin(dot.a * t)
        c.moveto(dot.item, dot.x, dot.y)
    root.after(20, motion)


def motion_inc():
    global t
    t += 0.2


def motion_dec():
    global t
    t -= 0.2


def stop():
    global stop_p
    stop_p = True
    return stop_p


motion()

button_stop = Button(root, text='Stop', width=15, height=3, bg='black', fg='red', font='arial 16', command=stop)
button_m_i = Button(root, text='M+', width=5, height=3, bg='black', fg='red', font='arial 14', command=motion_inc)
button_m_d = Button(root, text='M-', width=5, height=3, bg='black', fg='red', font='arial 14', command=motion_dec)
button_c_i = Button(root, text='C+', width=5, height=3, bg='black', fg='red', font='arial 14', command=create)
button_c_d = Button(root, text='C-', width=5, height=3, bg='black', fg='red', font='arial 14', command=remove)
button_m_i.grid(row=10, column=2, columnspan=1)
button_m_d.grid(row=11, column=2, columnspan=1)
button_stop.grid(row=10, column=3, rowspan=2, columnspan=4)
button_c_i.grid(row=10, column=7, columnspan=1)
button_c_d.grid(row=11, column=7, columnspan=1)

root.mainloop()
