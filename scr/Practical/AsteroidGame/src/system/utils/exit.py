import sys

from system.utils.file_manager import save_score, save_player_data
from system.object.program import get_program


def is_quit():
    save_score()
    get_program().current_player.options_settings.out()
    get_program().current_player.shop.out()
    save_player_data(get_program().current_player)
    sys.exit()

