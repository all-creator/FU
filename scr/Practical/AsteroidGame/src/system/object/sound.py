import pygame


class Sound:
    def __init__(self):
        self.on_focus = False
        self.on_click = False
        self.music = False
        self.on_click_sound = pygame.mixer.Sound("../res/music/click-on-button.ogg")
        self.on_focus_sound = pygame.mixer.Sound("../res/music/focus-on-button.ogg")

    def set_music(self, boolean):
        self.music = boolean

    def set_on_click(self, boolean):
        self.on_click = boolean

    def set_on_focus(self, boolean):
        self.on_focus = boolean

    def get_on_click_sound(self):
        if self.on_click:
            return self.on_click_sound
        else:
            return None

    def get_on_focus_sound(self):
        if self.on_focus:
            return self.on_focus_sound
        else:
            return None

    def play(self):
        self.stop()
        if self.music:
            pygame.mixer.music.load("../res/music/menu-sound-Incomplete.ogg", "ogg")
            pygame.mixer.music.play(-1, 0.0, 800)
            pygame.mixer.music.set_volume(0.6)

    def play_game(self):
        self.stop()
        if self.music:
            pygame.mixer.music.load("../res/music/game-sound-TakeMe.ogg", "ogg")
            pygame.mixer.music.play(-1, 0.0, 800)
            pygame.mixer.music.set_volume(0.6)

    @staticmethod
    def stop():
        pygame.mixer.music.stop()

