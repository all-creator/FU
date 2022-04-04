import random
import threading
from threading import Thread
from math import sin, cos, pi
from PIL import Image, ImageTk
from tkinter import Canvas, Tk, ALL
from time import sleep


class TrCanvas(Canvas):
    def create_rectangle(self, x1: int, y1: int, x2: int, y2: int, **kwargs):
        if "alpha" in kwargs:
            alpha = int(kwargs.pop("alpha") * 255)
            if "fill" in kwargs:
                fill = kwargs.pop("fill")
            else:
                fill = "white"
            fill = self.master.winfo_rgb(fill) + (alpha,)
            image = Image.new("RGBA", (x2 - x1, y2 - y1), fill)
            image = ImageTk.PhotoImage(image)
            self.create_image(x1, y1, image=image, anchor="nw")
        Canvas.create_rectangle(self, x1, y1, x2, y2, **kwargs)
        return image


class LivingEntity:
    def __init__(self, x, y, canvas, item, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.item = item
        self.area = canvas
        self.is_de_spawn = False
        Thread(target=self.__run__).start()

    def __run__(self):
        while not self.is_de_spawn:
            self.live()
            sleep(1 - self.speed)

    def live(self):
        self.de_spawn()

    def de_spawn(self):
        self.is_de_spawn = True
        self.area.delete(self.item)
        del self

    def move(self, x, y):
        self.x += x
        self.y += y
        self.area.move(self.item, x, y)


class Part(LivingEntity):

    def __init__(self, x, y, canvas, speed, radius, color):
        self.alpha = 0.7
        self.radius = radius
        self.color = color
        super().__init__(x, y, canvas, None, speed)

    def live(self):
        if self.alpha <= 0.2:
            self.de_spawn()
        self.alpha -= 0.025
        self.update()

    def update(self):
        self.area.delete(self.item)
        self.item = self.area.create_rectangle((self.x - self.radius + 1), self.y - 2,
                                               (self.x + self.radius), self.y + 2,
                                               fill=self.color, width=0, alpha=self.alpha)


class Fire(LivingEntity):
    def __init__(self, x, y, canvas, speed, radius, color):
        self.radius = radius
        self.color = color
        self.steps = []
        super().__init__(x, y, canvas, canvas.create_oval(x - radius, y - radius, x + radius,
                                                          y + radius, fill=color, outline=color), speed)

    def draw_particle(self):
        if len(self.steps) > 0:
            step = self.steps.pop(0)
            Part(step[0], step[1], self.area, self.speed, self.radius, self.color)

    def live(self):
        self.draw_particle()

    def move(self, x, y):
        if self.y % 4 == 0:
            self.steps.append((self.x, self.y))
        super().move(x, y)


class Firework(LivingEntity):
    def __init__(self, x_summon, color, radius, canvas, height_max, speed=0.995):
        self.color = color
        self.height = 0
        self.height_max = height_max
        self.parts = []
        super().__init__(x_summon, y_summon, canvas, Fire(x_summon, y_summon, canvas, speed, radius, color), speed)

    def de_spawn(self):
        super().de_spawn()

    def spawn_part(self):
        self.parts.append(Fire(self.x - random.randint(0, 10), self.item.y + random.randint(0, 10), self.area, self.speed, 2, self.color))
        self.parts.append(Fire(self.x - random.randint(0, 10), self.item.y - random.randint(0, 10), self.area, self.speed, 2, self.color))
        self.parts.append(Fire(self.x + random.randint(0, 10), self.item.y + random.randint(0, 10), self.area, self.speed, 2, self.color))
        self.parts.append(Fire(self.x + random.randint(0, 10), self.item.y - random.randint(0, 10), self.area, self.speed, 2, self.color))
        self.parts.append(Fire(self.x - random.randint(10, 20), self.item.y + random.randint(10, 20), self.area, self.speed, 2, self.color))
        self.parts.append(Fire(self.x - random.randint(10, 20), self.item.y - random.randint(10, 20), self.area, self.speed, 2, self.color))
        self.parts.append(Fire(self.x + random.randint(10, 20), self.item.y + random.randint(10, 20), self.area, self.speed, 2, self.color))
        self.parts.append(Fire(self.x + random.randint(10, 20), self.item.y - random.randint(10, 20), self.area, self.speed, 2, self.color))
        self.parts.append(Fire(self.x - random.randint(20, 50), self.item.y + random.randint(20, 50), self.area, self.speed, 2, self.color))
        self.parts.append(Fire(self.x - random.randint(20, 50), self.item.y - random.randint(20, 50), self.area, self.speed, 2, self.color))
        self.parts.append(Fire(self.x + random.randint(20, 50), self.item.y + random.randint(20, 50), self.area, self.speed, 2, self.color))
        self.parts.append(Fire(self.x + random.randint(20, 50), self.item.y - random.randint(20, 50), self.area, self.speed, 2, self.color))

    def fly(self):
        self.height += 1
        self.item.move(0, -2)

    def live(self):
        if len(self.parts) < 1:
            if self.height >= self.height_max:
                self.spawn_part()
                self.item.de_spawn()
            self.fly()
        else:
            for item in self.parts:
                item.move(0, 2)


y_summon = 580
r_w = 600

root = Tk()
tKCanvas = TrCanvas(root, width=r_w, height=r_w, bg="black")
tKCanvas.pack()
fireworks = []
colors = ['red', 'blue', 'yellow', 'pink', 'green', 'white', 'purple', 'gray', 'orange']


def generate():
    while True:
        x_summon = random.randint(50, 550)
        height = random.randint(60, 225)
        color = colors[random.randint(0, len(colors) - 1)]
        fireworks.append(Firework(x_summon, color, 4, tKCanvas, height))
        sleep(1)


def system_manager():
    while True:
        tKCanvas.delete(ALL)
        sleep(10)
        print("System refresh")


run = Thread(target=generate)
man = Thread(target=system_manager)
run.start()
man.start()

root.mainloop()
