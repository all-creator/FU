import math
import random
from tkinter import *


class Dot:

    def __init__(self, x, y, diam, color):
        self.item = c.create_oval(x - diam/2, y - diam/2, x + diam/2, y + diam/2, fill=color)
        self.x = x # х точки
        self.y = y # у точки
        self.a = 0 # угол
        self.pos = random.randint(5, 25) #сдвиг точек от круга


root = Tk()
r_w = 600 #окно
r_b_b = 150 #радиус большого круга
c = Canvas(root, width=r_w, height=r_w, bg="white")
c.grid(row=0, rowspan=10, column=0, columnspan=10)

ball = c.create_oval(r_w / 2 + r_b_b, r_w / 2 + r_b_b, r_w / 2 - r_b_b, r_w / 2 - r_b_b, fill='black')

x0 = 280 #нулевая координата х
y0 = 40 #нулевая координаа у
d = 30 #диаметр
t = 1 #угловая скорость
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
        dot.x = ((290 + dot.pos) - d / 2) + ((200 + dot.pos) + d) * math.cos(dot.a * t)#отрисовка точки по диаметру большого круга
        dot.y = ((290 + dot.pos) - d / 2) + ((200 + dot.pos) + d) * math.sin(dot.a * t)
        c.moveto(dot.item, dot.x, dot.y)
    root.after(20, motion)


def motion_inc():
    global t
    t += 0.2 # скорость


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
