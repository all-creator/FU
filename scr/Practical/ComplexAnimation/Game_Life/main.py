from tkinter import Canvas, Tk

r_w = 600
root = Tk()
canvas = Canvas(root, width=r_w, height=r_w, bg="black")
canvas.pack()


class Map:
    def __init__(self):
        self.block_size = 20
        self.r = r_w

    def gen(self):
        x = 2
        y = 2
        block_line = int(self.r / self.block_size)
        for _ in range(0, block_line):
            for _ in range(0, block_line):
                Block(x, y, self.block_size)
                x += self.block_size
            y += self.block_size
            x = 2


class Block:
    def __init__(self, x, y, size):
        self.is_lived = False
        if size % 2 != 0:
            size -= 1
        self.padding = 1
        self.x = size-self.padding
        self.y = size-self.padding
        canvas.create_rectangle(x, y, self.x + x, self.y + y, width=self.padding, fill='white', outline='black')


Map().gen()

root.mainloop()
