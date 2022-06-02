from game.meta.meta import MetaObject

from gui.enums import shop_screen
from system.object.display import dp_w, dp_h, adaptive_font
from gui.object.menu import ImgButton, Label, Img
from gui.object.animations import Scale


class Shop:
    def __init__(self, money=0):
        self.money = money
        self.meta = MetaObject()
        self.left_img: ImgButton = None
        self.right_img: ImgButton = None

    def get_money(self):
        return self.money

    def inc_money(self, money):
        self.money += money

    def set_money(self, money):
        self.money = money

    def dec_money(self, money):
        self.money -= money

    def init(self):
        self.left_img = ImgButton("../res/shop/left-icon.png", size=[dp_w(3), dp_h(5)], pos=[dp_w(4), dp_h(15)])
        self.right_img = ImgButton("../res/shop/right-icon.png", size=[dp_w(3), dp_h(5)], pos=[dp_w(30.5), dp_h(15)])
        shop_screen[0].add(self.right_img)
        shop_screen[0].add(self.left_img)
        self.init_money_icons()
        shop_screen[0].resize_bg()

    def init_money_icons(self):
        w_s = 34
        if self.money > 100:
            w_s -= 1
        if self.money > 1000:
            w_s -= 1
        mon_ico = Img("../res/shop/coin.png", pos=[dp_w(w_s), 0])
        scale = Scale(mon_ico, 0.5)
        scale.active()
        shop_screen[0].add(scale.item)
        shop_screen[0].add(Label(text=str(self.money), pos=[dp_w(w_s+3), dp_h(0.5)], font_size=adaptive_font(1.4)))

    def out(self):
        self.left_img = None
        self.right_img = None
