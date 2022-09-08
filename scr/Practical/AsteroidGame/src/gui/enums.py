menu_bg = "../res/bg/bg-menu.png"

menus_screen = []

auth_screen = []

option_screen = []

shop_screen = []

game_screen = []

active_screen = auth_screen


def set_active_screen(screen_):
    global active_screen
    active_screen = screen_


def get_active_screen():
    global active_screen
    return active_screen
