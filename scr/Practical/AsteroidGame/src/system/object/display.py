import pygame

pygame.init()

f'''
Представляет обёрнутый объект экрана: {pygame.display}

    Атрибуты:
    info - представление информации дисплея: {pygame.display.Info}
    size - объединённые параметры (высота, ширина) экрана
'''


class Display:
    def __init__(self):
        self.info = pygame.display.Info()
        self.size = (self.info.current_w, self.info.current_h)


f'''
Представляет обёрнутый объект окна: {pygame.Surface}

    Аргументы:
    is_full_screen - определяет будет ли развёрнута игра на весь экран
    size - устанавливает ширину и высоту рабочего окна
'''


class Screen:
    def __init__(self, size, is_full_screen=True):
        if is_full_screen:
            self.item = pygame.display.set_mode(size, flags=pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
        else:
            self.item = pygame.display.set_mode(size)


display = Display()
__default_screen: Screen

'''
Генерирует окно по умолчанию

    Аргументы:
    size - размеры окна (ширина, высота)
    ?is_full_screen - определяет будет ли окно на весь экран
'''


def gen_screen(size, is_full_screen=True):
    global __default_screen, __dp_w, __dp_h
    __default_screen = Screen(size, is_full_screen)
    __dp_w = get_default_screen().get_width() // 64
    __dp_h = get_default_screen().get_height() // 64
    return __default_screen.item


'''Возвращает окно по умолчанию'''


def get_default_screen(): return __default_screen.item


__dp_w = 0
__dp_h = 0


def dp_w(mult=1): return __dp_w * mult
def dp_h(mult=1): return __dp_h * mult


def adaptive_font(mult=1): return int((dp_w() + dp_h()) * mult)
