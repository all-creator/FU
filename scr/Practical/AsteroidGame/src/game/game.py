from gui.enums import set_active_screen, menus_screen, game_screen
from system.object.display import dp_w
from gui.object.menu import adaptive_font, Label, Menu
from system.enums import font, sound
from system.utils.file_manager import score
from game.utils import gen_dynamic_bg
import pygame

font_size = adaptive_font(0.9)
menu = Menu(border=[0, 0])
game_screen.append(menu)


class Game:

    def __init__(self, player):
        self.player = player
        self.load = False
        self.asteroid_group = set([])
        self.missile_group = set([])
        self.lives = 3
        self.score = 0
        self.lives_label = Label(text="Жизни: " + str(self.lives), is_sys_font=False, font=font, font_size=font_size)
        self.score_label = Label(text="Счёт: " + str(self.score), pos=[dp_w(50), 0], is_sys_font=False, font=font,
                                 font_size=font_size)
        menu.add(self.lives_label)
        menu.add(self.score_label)

    def start(self):
        from system.enums import bg, screen
        set_active_screen(game_screen)
        bg.img = pygame.image.load("../res/bg/bg-game.jpg")
        bg.resize(screen.get_width(), screen.get_height())
        gen_dynamic_bg(bg, screen)
        sound.play_game()
        self.load = True

    def render(self):
        if not self.load:
            return

    def inc_lives(self):
        self.lives += 1
        self.lives_label.update_text("Жизни: " + str(self.lives))

    def dec_lives(self):
        self.lives -= 1
        self.lives_label.update_text("Жизни: " + str(self.lives))

    def add_score(self, added):
        self.score += added
        self.score_label.update_text("Счёт: " + str(self.score))

    def stop(self):
        from system.enums import bg, screen
        set_active_screen(menus_screen)
        bg.img = pygame.image.load("../res/bg/bg-root.png")
        bg.resize(screen.get_width(), screen.get_height())
        score.setdefault(self.player.name, self.score)
        self.load = False
