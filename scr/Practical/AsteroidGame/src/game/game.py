import random

import pygame

from game.utils import gen_dynamic_bg
from gui.enums import set_active_screen, menus_screen, game_screen
from gui.object.menu import adaptive_font, Label, Menu
from system.enums import font, sound
from system.object.display import dp_w
from system.utils.file_manager import score
from game.game_object import Asteroid
from game.utils import group_collide, group_group_collide

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
        self.ship = player.get_active_ship()
        self.ship.missile_group = self.missile_group
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

    def render(self, screen):
        self.ship.render(screen)
        self.ship.update()
        for item in self.missile_group:
            item.render(screen)
            item.update()
        for item in self.asteroid_group:
            item.render(screen)
            item.update()

        if group_collide(self.asteroid_group, self.ship) > 0:
            if self.lives > 1:
                self.dec_lives()
            else:
                self.stop()

        hits = group_group_collide(self.asteroid_group, self.missile_group)
        self.add_score(hits * 100)

    def inc_lives(self):
        self.lives += 1
        self.lives_label.update_text("Жизни: " + str(self.lives))

    def dec_lives(self):
        self.lives -= 1
        self.lives_label.update_text("Жизни: " + str(self.lives))

    def add_score(self, added):
        self.score += added
        self.score_label.update_text("Счёт: " + str(self.score))

    def gen_asteroid(self):
        from system.enums import screen
        x = random.randint(0, screen.get_width())
        y = random.randint(0, screen.get_height())
        s_x = self.ship.pos[1]
        s_y = self.ship.pos[0]
        vel = [random.random() * 7, random.random() * 7]
        if s_x + 100 < x and s_y + 100 < y and len(self.asteroid_group) < 32:
            self.asteroid_group.add(Asteroid(pos=[x, y], ang_vel=(random.random() * 5), vel=vel, ang=0))

    def stop(self):
        from system.enums import bg, screen
        set_active_screen(menus_screen)
        bg.img = pygame.image.load("../res/bg/bg-root.jpeg")
        bg.resize(screen.get_width(), screen.get_height())
        score.setdefault(self.player.name, self.score)
        self.load = False
