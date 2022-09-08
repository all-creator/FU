import pygame


class Sound:
    def __init__(self):
        self.is_sound = False
        self.music = False
        self.on_click_sound = pygame.mixer.Sound("../res/music/click-on-button.ogg")
        self.on_click_sound.set_volume(0.9)
        self.on_focus_sound = pygame.mixer.Sound("../res/music/focus-on-button.ogg")
        self.on_focus_sound.set_volume(0.9)
        self.ship_active = pygame.mixer.Sound("../res/music/ship-active.ogg")
        self.ship_active.set_volume(0.4)
        self.missile = pygame.mixer.Sound("../res/music/missile-sound.ogg")
        self.missile.set_volume(0.6)

    def set_music(self, boolean):
        self.music = boolean

    def set_sound(self, boolean):
        self.is_sound = boolean

    def get_on_click_sound(self):
        if self.is_sound:
            return self.on_click_sound
        else:
            return None

    def get_on_focus_sound(self):
        if self.is_sound:
            return self.on_focus_sound
        else:
            return None

    def get_active_ship_sound(self):
        if self.is_sound:
            return self.ship_active
        else:
            return None

    def get_missile_sound(self):
        if self.is_sound:
            return self.missile
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

