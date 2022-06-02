from game.options import Options
from game.shop import Shop


class Player:
    def __init__(self, nick):
        self.name = nick
        self.options_settings = Options()
        self.shop = Shop()

    def get_player_data(self):
        return f"nick: {self.name}"

    def __str__(self):
        return self.name

