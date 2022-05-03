import sys

import pygame

from object.menu import Label, Menu, Button
from system.object.background import Background
from object.animator import Event
from system.object.scheduler_pool import Scheduler
from system.object.display import gen_screen, dp_h, dp_w, adaptive_font, display
from system.utils.time_utils import current_milli_time
from system.utils.file_manager import load_score, save_score

pygame.init()

size = width, height = display.size

screen = gen_screen(size)

bg = Background("../res/bg/bg-root.jpeg")


def pars_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            is_mouse_press()
    mouse_weight, mouse_height = pygame.mouse.get_pos()
    for button in main_menu.get_buttons():
        if button.pos[0] < mouse_weight < button.get_left_pos()[0] and button.pos[1] < mouse_height < \
                button.get_left_pos()[1]:
            if not button.is_focus:
                Event(button, button.focused)
        else:
            if button.is_focus:
                Event(button, button.dis_focus)


def is_quit():
    save_score()
    sys.exit()


millis = current_milli_time()
real_millis = current_milli_time()
s_millis = current_milli_time()
t = 0

main_menu = Menu(main_pos=[dp_w(8), dp_h(8)])
score_menu = Menu(main_pos=[dp_w(46), dp_h(12)], bg="../res/bg/bg-menu.png")

main_menu.add(Label(text="Астероиды", font='noteworthy', font_size=adaptive_font(2),
                    ))
main_menu.add(Button(pos=[0, dp_h(12)], text="Начать Игру", font='rockwell',
                     ))
main_menu.add(Button(pos=[0, dp_h(20)], text="Магазин", font='rockwell',
                     ))
main_menu.add(Button(pos=[0, dp_h(28)], text="Настройки", font='rockwell',
                     ))
main_menu.add(Button(pos=[0, dp_h(36)], text="Выход", font='rockwell', on_click=is_quit,
                     ))
score_menu.add(Label(pos=[0, 0], text="Таблицы лидеров", color=(240, 240, 0), font='thonburi'))


def is_mouse_press():
    global main_menu
    mouse_weight, mouse_height = pygame.mouse.get_pos()
    for button in main_menu.get_buttons():
        if button.pos[0] < mouse_weight < button.get_left_pos()[0] and button.pos[1] < mouse_height < \
                button.get_left_pos()[1]:
            Event(button, button.clicked)


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


def fps():
    global t
    print(f"FPS: {t}")
    t = 0


u = 1
def test():
    global main_menu, u
    if u <= 100:
        u += 0.1
    else:
        u -= 0.1
    for b in main_menu.get_buttons():
        b.item = pygame.transform.smoothscale(b.item, (dp_w(12) + u, dp_h(4) + u))


def app():
    tick = 1000 // 60
    global millis, t, s_millis
    pygame.mixer.music.load("../res/music/menu-sound-Incomplete.ogg", "ogg")
    pygame.mixer.music.play(-1, 0.0, 800)
    pygame.mixer.music.set_volume(0.6)
    gen_score()
    while True:
        if current_milli_time() >= millis + tick:
            pars_event()

            t += 1
            millis = current_milli_time()

            bg.render(screen)

            # !sfcompact (noteworthy) ?rockwell (thonburi)

            main_menu.render(screen)
            score_menu.render(screen)

            test()

            pygame.display.flip()
        if current_milli_time() >= s_millis + 1000:
            fps()
            s_millis = current_milli_time()


if __name__ == '__main__':
    app()
