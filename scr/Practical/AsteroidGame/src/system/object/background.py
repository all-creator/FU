import pygame
from system.object.display import get_default_screen

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
    def __init__(self, img="", scale_size=None, pos=None):
        if scale_size is None:
            scale_size = get_default_screen().get_size()
        if pos is None:
            pos = [0, 0]
        self.img = pygame.image.load(img)
        self.img = pygame.transform.scale(self.img, scale_size)
        self.pos = pos

    '''
    Отображает задний фон

        Аргументы:
        screen - окно в котором будет установлен задний фон
    '''

    def render(self, screen):
        screen.blit(self.img, self.pos)

    def resize(self, w, h):
        self.img = pygame.transform.scale(self.img, (w, h))
