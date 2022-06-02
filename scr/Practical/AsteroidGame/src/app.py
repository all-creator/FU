import pygame

from system.utils.time_utils import current_milli_time
from system.utils.event import pars_event
from gui.init import gen_score
from gui.enums import get_active_screen
from system.enums import screen, bg
from system.object.program import get_program

millis = current_milli_time()
real_millis = current_milli_time()
s_millis = current_milli_time()
t = 0

pygame.init()


def fps():
    global t
    print(f"FPS: {t}")
    t = 0


def app():
    tick = 1000 // 60
    global millis, t, s_millis
    gen_score()
    while True:
        if current_milli_time() >= millis + tick:

            pars_event()

            t += 1
            millis = current_milli_time()

            bg.render(screen)

            get_program().game.render()

            for menu in get_active_screen():
                menu.render(screen)

            pygame.display.flip()
        if current_milli_time() >= s_millis + 1000:
            fps()
            s_millis = current_milli_time()


if __name__ == '__main__':
    app()
