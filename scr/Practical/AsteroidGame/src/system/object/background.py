import pygame
from system.object.display import get_default_screen, dp_h, dp_w

f'''
Создаёт объект заднего фона

    Аргументы:
    img - путь к картинке заднего фона
    --------------------------
    Атрибуты:
    img - представление картинки заднего фона в pygame: {pygame.Surface}
    pos - относительные координаты: для заднего фона всегда [0, 0]
'''


class Background:
    def __init__(self, img, scale_size=None, pos=None):
        if scale_size is None:
            scale_size = get_default_screen().get_size()
        if pos is None:
            pos = [0, 0]
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, scale_size)
        self.pos = pos
        self.items = []

    '''
    Отображает задний фон

        Аргументы:
        screen - окно в котором будет установлен задний фон
    '''

    def render(self, screen):
        screen.blit(self.img, self.pos)
        for i in self.items:
            i.move()
            i.render(screen)

    def resize(self, w, h):
        self.img = pygame.transform.scale(self.img, (w, h))


class DynamicBackgroundItem:
    def __init__(self, img, scale_size=None, pos=None, vector=None):
        if scale_size is None:
            scale_size = [dp_w(2), dp_h(2)]
        if pos is None:
            pos = [0, 0]
        if vector is None:
            vector = [0, 0]
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, scale_size)
        self.pos = pos
        self.start_pos = pos
        self.vector = vector

    def move(self):
        self.pos = [self.pos[0] + self.vector[0], self.pos[1] + self.vector[1]]
        if self.pos[1] > get_default_screen().get_height() or self.pos[0] > get_default_screen().get_width():
            self.pos = self.start_pos

    def render(self, screen):
        screen.blit(self.img, self.pos)
