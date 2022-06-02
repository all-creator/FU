from game.auth import Authorization
from game.program import get_program
from gui.object.animations import Scale
from gui.object.animator import IS_FOCUS, DIS_FOCUS, SPAWN
from gui.object.menu import Label, Menu, Button, InputBox, Img, ImgButton
from system.object.display import dp_h, dp_w, adaptive_font
from system.utils.exit import is_quit
from system.utils.file_manager import load_score
from gui.enums import menus_screen, option_screen, auth_screen, menu_bg, set_active_screen, shop_screen

"""
==========================================
================Методы====================
==========================================
"""

# Генерация списка таблицы лидеров


def gen_score():
    pad = 6
    index = 1
    scores = load_score()
    for name, score in scores.items():
        if index > 10:
            break
        score_menu.add(Label(pos=[0, dp_h(pad)], text=f"{index}. {name}: {score}", color=(240, 240, 0),
                             font='thonburi', font_size=adaptive_font(0.8)))
        index += 1
        pad += 4
    score_menu.resize_bg()


def on_main_screen():
    set_active_screen(menus_screen)


def on_option_screen():
    set_active_screen(option_screen)


def on_shop_screen():
    set_active_screen(shop_screen)


def on_game():
    get_program().game.start()


def on_auth(args):
    auth.authorization(args[0]())
    args[1](f"account: {get_program().current_player}")
    on_main_screen()


"""
==========================================
===============Элементы===================
==========================================
"""

# Главное меню
main_menu = Menu(main_pos=[dp_w(8), dp_h(8)])
menus_screen.append(main_menu)

# Заголовок - название игры
main_menu.add(Label(text="Астероиды", font='noteworthy', font_size=adaptive_font(2)))

# Кнопка Начать игру
new_game_button = Button(pos=[0, dp_h(12)], text="Начать Игру", font='rockwell', on_click=on_game)
scale = Scale(new_game_button, 1.2)
new_game_button.animator.bind(scale, IS_FOCUS)
new_game_button.animator.bind(scale, DIS_FOCUS)
main_menu.add(new_game_button)

# Кнопка Магазин
shop_button = Button(pos=[0, dp_h(20)], text="Магазин", font='rockwell', on_click=on_shop_screen)
scale = Scale(shop_button, 1.2)
shop_button.animator.bind(scale, IS_FOCUS)
shop_button.animator.bind(scale, DIS_FOCUS)
main_menu.add(shop_button)

# Кнопка Настройки
options_button = Button(pos=[0, dp_h(28)], text="Настройки", font='rockwell', on_click=on_option_screen)
scale = Scale(options_button, 1.2)
options_button.animator.bind(scale, IS_FOCUS)
options_button.animator.bind(scale, DIS_FOCUS)
main_menu.add(options_button)

# Кнопка Выход
exit_button = Button(pos=[0, dp_h(36)], text="Выход", font='rockwell', on_click=is_quit)
scale = Scale(exit_button, 1.2)
exit_button.animator.bind(scale, IS_FOCUS)
exit_button.animator.bind(scale, DIS_FOCUS)
main_menu.add(exit_button)

# Меню счёта
score_menu = Menu(main_pos=[dp_w(46), dp_h(12)], bg=menu_bg)
menus_screen.append(score_menu)

# Заголовок таблицы лидеров
score_menu.add(Label(pos=[0, 0], text="Таблицы лидеров", color=(240, 240, 0), font='thonburi'))

# Нижний артикул
info = Menu(main_pos=[0, dp_h(60)], bg=menu_bg)
menus_screen.append(info)
auth_screen.append(info)

info.add(Label(text=f"version: {get_program().version}", font_size=adaptive_font(0.7)))
info_account = Label(pos=[0, dp_h(2)], text=f"account: {get_program().current_player}", font_size=adaptive_font(0.7))
info.add(info_account)

info.resize_bg()

# Меню авторизации
auth_menu = Menu(main_pos=[dp_w(28), dp_h(28)], bg=menu_bg)
auth_screen.append(auth_menu)

auth = Authorization(auth_menu)

auth_menu.add(Label(text="Введите ваш ник", font_size=adaptive_font(1.2)))
auth_input = InputBox(pos=[0, dp_h(3)], active=True, color=(240, 240, 0))
auth_menu.add(auth_input)
auth_menu.add(Button(pos=[dp_w(2), dp_h(6)], text="Продолжить", on_click=on_auth,
                     on_click_params=[auth_input.get_text, info_account.update_text]))

auth_menu.resize_bg()

# Меню настроек
options_menu = Menu(main_pos=[dp_w(28), dp_h(28)], bg=menu_bg)
option_screen.append(options_menu)

options_menu.add(Label(text="Настройки", font_size=adaptive_font(1.5)))
options_menu.add(Button(pos=[dp_w(2), dp_h(10)], text="Назад", on_click=on_main_screen, font_size=adaptive_font(1.2)))

options_menu.resize_bg()

# Меню магазина
shop_menu = Menu(main_pos=[dp_w(13), dp_h(16)], bg=menu_bg)
shop_screen.append(shop_menu)

shop_menu.add(Label(text="Магазин", font_size=adaptive_font(1.6)))

shop_start_ship_img = Img("../res/ships/start-ship.png", pos=[dp_w(14), dp_h(6)])
scale = Scale(shop_start_ship_img, 0.25)
scale.active()
shop_start_ship_img = scale.item
shop_menu.add(shop_start_ship_img)

shop_menu.add(Label(text="Куплено", pos=[dp_w(16.4), dp_h(27)], font_size=adaptive_font(1.2), color=(170, 170, 170)))

shop_menu.add(Button(pos=[dp_w(17), dp_h(32)], text="Назад", on_click=on_main_screen, font_size=adaptive_font(1.2)))

shop_menu.resize_bg()
