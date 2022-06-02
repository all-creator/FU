import pygame


class Animation:
    def __init__(self, item):
        self.item = item

    def animate(self):
        return


class ComplexAnimation(Animation):
    def __init__(self, item):
        super().__init__(item)
        self.is_active = False

    def animate(self):
        if self.is_active:
            self.is_active = False
            self.dis_active()
        else:
            self.is_active = True
            self.active()

    def active(self):
        return

    def dis_active(self):
        return


class Scale(ComplexAnimation):
    def __init__(self, item, amount):
        super().__init__(item=item)
        self.amount = amount
        self.instance = item.item

    def active(self):
        self.item.item = pygame.transform.smoothscale(self.item.item, (self.item.weight() * self.amount,
                                                                       self.item.height() * self.amount))

    def dis_active(self):
        self.item.item = self.instance
