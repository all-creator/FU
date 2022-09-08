import pygame

from system.object.display import dp_w, dp_h, adaptive_font
from system.utils.id_utils import auto_generate_id
from system.object.background import Background
from gui.object.animator import Animator, Event
from system.enums import sound


class MenuObject:
    def __init__(self, id_=None, pos=None):
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
        self.animator = Animator(self)

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
    def __init__(self, id_=None, pos=None, text="", font=None, font_size=None, color=(255, 255, 255), is_sys_font=True):
        super().__init__(id_=id_, pos=pos)
        if font_size is None:
            font_size = adaptive_font()
        self.text = text
        self.font = font
        self.font_size = font_size
        self.color = color
        if is_sys_font:
            self.font_item = pygame.font.SysFont(self.font, self.font_size)
        else:
            self.font_item = pygame.font.Font(self.font, self.font_size)
        self.item = self.font_item.render(self.text, True, self.color)
        Event(self, self.is_load)

    def update_text(self, text):
        self.text = text
        self.item = self.font_item.render(self.text, True, self.color)


class Img(MenuObject):
    def __init__(self, img: str, id_=None, pos=None, size=None):
        super().__init__(id_=id_, pos=pos)
        self.image = img
        self.size = size
        if self.size is not None:
            self.item = pygame.transform.scale(pygame.image.load(self.image), self.size)
        else:
            self.item = pygame.image.load(self.image)
        Event(self, self.is_load)


class Button(Label):
    def __init__(self, id_=None, pos=None, text="", font=None, font_size=None, color=(255, 255, 255), on_click=None,
                 on_focus=None, on_click_params=None):
        super().__init__(id_=id_, pos=pos, text=text, font=font, font_size=font_size, color=color)
        self.on_click = on_click
        self.on_focus = on_focus
        self.is_focus = False
        self.params = on_click_params

    def clicked(self):
        if self.is_killed:
            return
        if self.on_click:
            self.on_click.run()
        if sound.get_on_click_sound() is not None:
            sound.get_on_click_sound().play()

    def focused(self):
        if self.is_killed:
            return
        if not self.is_focus:
            self.is_focus = True
            if self.on_focus is not None:
                self.on_focus(self)
            if sound.get_on_focus_sound() is not None:
                sound.get_on_focus_sound().play()

    def dis_focus(self):
        self.is_focus = False


class ImgButton(Button):
    def __init__(self, img: str, id_=None, pos=None, on_click=None, on_focus=None, on_click_params=None, size=None):
        super().__init__(id_=id_, pos=pos, on_click=on_click, on_click_params=on_click_params, on_focus=on_focus)
        self.image = img
        if size is None:
            size = [0, 0]
        self.size = size
        self.item = pygame.transform.scale(pygame.image.load(self.image), self.size)
        Event(self, self.is_load)


class InputBox(Label):
    def __init__(self, id_=None, pos=None, text="", font=None, font_size=None, color=(255, 255, 255), rect=None,
                 active=False, on_return_pressed=None):
        super().__init__(id_=id_, pos=pos, text=text, font=font, font_size=font_size, color=color)
        self.rect = rect
        self.active = active
        self.on_return = on_return_pressed

    def set_on_return_pressed(self, on_return_pressed):
        self.on_return = on_return_pressed

    def handle_event(self, event):
        if self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                if event.key != pygame.K_RETURN:
                    self.text += event.unicode
                else:
                    self.on_return.run()
            self.item = self.font_item.render(self.text, True, self.color)

    def render(self, screen):
        screen.blit(self.item, self.pos)
        if self.rect is not None:
            pygame.draw.rect(screen, self.color, self.rect, 2)

    def update(self):
        width = max(200, self.item.get_width()+10)
        self.rect.w = width

    def get_text(self):
        return self.text


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
        self.inputBoxs = []
        if bg is not None:
            self.set_bg(bg)

    def render(self, screen):
        if not self.is_killed:
            self.render_bg(screen)
            for child in self.child:
                child.render(screen)

    def add(self, child: MenuObject):
        if type(child) is Button or type(child) is ImgButton:
            self.buttons.append(child)
        if type(child) is InputBox:
            self.inputBoxs.append(child)
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

    def get_input_boxs(self):
        return self.inputBoxs
