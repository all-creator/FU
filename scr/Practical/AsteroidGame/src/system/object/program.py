from system.utils.file_manager import load_data, load_player_data
from game.game import Game

program = None


class Program:
    def __init__(self, version):
        self.version = version
        self.current_player = None
        self.game = None

    def set_player(self, player):
        self.current_player = load_player_data(player)
        self.current_player.set_default_ship()
        self.current_player.options_settings.init()
        self.current_player.shop.init()
        self.game = Game(self.current_player)


def get_program():
    global program
    return program if program is not None else gen_program()


def gen_program():
    global program
    program = Program(load_data()["version"])
    return program

