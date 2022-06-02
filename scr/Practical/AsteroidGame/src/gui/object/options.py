import pygame

from system.object.display import dp_w, dp_h
from system.utils.function import Function
from gui.object.menu import ImgButton
from gui.enums import option_screen
from system.enums import sound


class Options:
    def __init__(self):
        self.music = True
        self.sound = True
        self.music_img: ImgButton = None
        self.sound_img: ImgButton = None

    def get_sound_img(self):
        if self.sound:
            return "../res/options/sound-on.png"
        return "../res/options/sound-off.png"

    def get_music_img(self):
        if self.music:
            return "../res/options/music-on.png"
        return "../res/options/music-off.png"

    def switch_sound(self):
        if self.sound:
            self.disable_sound()
        else:
            self.enable_sound()
        sound.set_on_click(self.sound)
        sound.set_on_focus(self.sound)
        self.sound_img.item = pygame.transform.scale(pygame.image.load(self.get_sound_img()), self.sound_img.size)

    def switch_music(self):
        if self.music:
            self.disable_music()
        else:
            self.enable_music()
        self.music_img.item = pygame.transform.scale(pygame.image.load(self.get_music_img()), self.music_img.size)

    def disable_music(self):
        self.music = False
        sound.set_music(self.music)
        sound.stop()

    def enable_music(self):
        self.music = True
        sound.set_music(self.music)
        sound.play()

    def disable_sound(self):
        self.sound = False

    def enable_sound(self):
        self.sound = True

    def init(self):
        self.music_img = ImgButton(self.get_music_img(), pos=[0, dp_h(4)], size=[dp_w(3), dp_w(3)],
                                   on_click=Function(self.switch_music))
        self.sound_img = ImgButton(self.get_sound_img(), pos=[dp_w(5), dp_h(4)], size=[dp_w(3), dp_w(3)],
                                   on_click=Function(self.switch_sound))
        option_screen[0].add(self.music_img)
        option_screen[0].add(self.sound_img)
        sound.set_on_click(self.sound)
        sound.set_on_focus(self.sound)
        sound.set_music(self.music)

    def out(self):
        self.music_img = None
        self.sound_img = None
