import pygame

from system.object.display import dp_w, dp_h, adaptive_font
from system.utils.id_utils import auto_generate_id
from system.object.background import Background
from object.animator import Animator, Event

on_click_sound = pygame.mixer.Sound("../res/music/click-on-button.ogg")
on_focus_sound = pygame.mixer.Sound("../res/music/focus-on-button.ogg")


class MenuObject:
    def __init__(self, id_=None, pos=None, animator=None):
        if pos is None:
            pos = [0, 0]
        if id_ is None:
            id_ = auto_generate_id()
        self.child = []
        self.id = id_
        self.pos = pos
        self.item = None
        self.is_killed = False
        self.animator = None
        if animator is not None:
            self.animator = Animator(self, animator)

    def weight(self):
        return self.item.get_size()[0]

    def height(self):
        return self.item.get_size()[1]

    def render(self, screen):
        screen.blit(self.item, self.pos)

    def get_left_pos(self):
        return self.weight() + self.pos[0], self.height() + self.pos[1]

    def kill(self):
        self.is_killed = True

    def is_load(self):
        return

    def focused(self):
        return

    def dis_focus(self):
        return


class Label(MenuObject):
    def __init__(self, id_=None, pos=None, text="", font='', font_size=None, color=(255, 255, 255), animator=None):
        super().__init__(id_=id_, pos=pos, animator=animator)
        if font_size is None:
            font_size = adaptive_font()
        self.text = text
        self.font = font
        self.font_size = font_size
        self.color = color
        font = pygame.font.SysFont(self.font, self.font_size)
        self.item = font.render(self.text, True, self.color)
        Event(self, self.is_load)


class Button(Label):
    def __init__(self, id_=None, pos=None, text="", font='', font_size=None, color=(255, 255, 255), on_click=None,
                 on_focus=None, animator=None):
        super().__init__(id_=id_, pos=pos, text=text, font=font, font_size=font_size, color=color, animator=animator)
        self.on_click = on_click
        self.on_focus = on_focus
        self.is_focus = False

    def clicked(self):
        if self.is_killed:
            return
        on_click_sound.play()
        if self.on_click is not None:
            self.on_click()

    def focused(self):
        if self.is_killed:
            return
        if not self.is_focus:
            self.is_focus = True
            on_focus_sound.play()
            if self.on_focus is not None:
                self.on_focus(self)

    def dis_focus(self):
        self.is_focus = False


class Menu(MenuObject):
    def __init__(self, main_pos=None, border=None, bg=None):
        super().__init__()
        if main_pos is None:
            main_pos = [dp_w(4), dp_h(4)]
        if border is None:
            border = [dp_w(2), dp_h(1.5)]
        self.main_pos = main_pos
        self.border = border
        self.bg = None
        self.weight = 0
        self.height = 0
        self.buttons = []
        if bg is not None:
            self.set_bg(bg)

    def render(self, screen):
        if not self.is_killed:
            self.render_bg(screen)
            for child in self.child:
                child.render(screen)

    def add(self, child: MenuObject):
        if type(child) is Button:
            self.buttons.append(child)
        self.norm(child)
        self.weight = max(self.weight, child.get_left_pos()[0])
        self.height = max(self.height, child.get_left_pos()[1])
        self.child.append(child)

    def norm(self, child: MenuObject):
        child.pos = [child.pos[0] + self.main_pos[0], child.pos[1] + self.main_pos[1]]

    def kill(self):
        super().kill()
        for b in self.buttons:
            b.kill()

    def set_bg(self, bg: str):
        self.bg = Background(bg, pos=[self.main_pos[0] - self.border[0], self.main_pos[1] - self.border[1]])

    def render_bg(self, screen):
        if self.bg is not None:
            self.bg.render(screen)

    def resize_bg(self):
        self.bg.resize(self.weight - self.main_pos[0] + self.border[0] * 2,
                       self.height - self.main_pos[1] + self.border[1] * 2)

    def get_buttons(self):
        return self.buttons
