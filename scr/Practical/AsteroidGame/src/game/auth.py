from game.program import get_program
from system.enums import sound


class Authorization:
    def __init__(self, menu):
        self.player = ""
        self.is_auth = False
        self.auth_menu = menu

    def get_auth(self):
        return self.is_auth

    def authorization(self, player):
        self.player = player
        self.is_auth = True
        get_program().set_player(self.player)
        sound.play()

