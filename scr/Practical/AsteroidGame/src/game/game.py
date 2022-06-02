from gui.enums import set_active_screen, menus_screen
import pygame


class Game:
    def __init__(self, player):
        self.player = player
        self.load = False

    def start(self):
        from system.enums import bg, screen
        set_active_screen([])
        bg.img = pygame.image.load("../res/bg/bg-game.png")
        bg.resize(screen.get_width(), screen.get_height())

    def render(self):
        if not self.load:
            return

    def stop(self):
        from system.enums import bg, screen
        set_active_screen(menus_screen)
        bg.img = pygame.image.load("../res/bg/bg-root.png")
        bg.resize(screen.get_width(), screen.get_height())