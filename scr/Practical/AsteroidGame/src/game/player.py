import pygame

from gui.object.options import Options
from gui.object.shop import Shop
from system.object.display import dp_w, dp_h
from game.ship import Ship
from game.utils import load_img
from game.game_object import ImgMeta


class Player:
    def __init__(self, nick):
        self.name = nick
        self.options_settings = Options()
        self.shop = Shop()
        self.ship = None

    def get_player_data(self):
        return f"nick: {self.name}"

    def __str__(self):
        return self.name

    def get_active_ship(self):
        return self.ship

    def set_default_ship(self):
        img: pygame.Surface = load_img("../res/ships/asteroid-ship.png", 0.2)
        w = img.get_width() - 256
        h = img.get_height() - 256
        self.ship = Ship([dp_w(28), dp_h(28)], [0, 0], img,
                         load_img("../res/ships/asteroid-ship-active.png", 0.2),
                         ImgMeta([w/2, h/2], [w,  h], (w/2+h/2)/2))
