import pygame

from gui.object.animator import Event
from gui.enums import get_active_screen
from system.utils.exit import is_quit
from system.object.program import get_program


def pars_event():
    mouse_weight, mouse_height = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_quit()
        if get_program().game and get_program().game.load:
            if event.type == pygame.KEYDOWN:
                is_key_press_in_game(event, get_program().game)
            elif event.type == pygame.KEYUP:
                is_key_un_press_in_game(event, get_program().game)
        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_mouse_press(mouse_weight, mouse_height)
            elif event.type == pygame.KEYDOWN:
                is_key_press(event)
    is_mouse_focus(mouse_weight, mouse_height)


def is_mouse_focus(mouse_weight, mouse_height):
    for menu in get_active_screen():
        if not menu.is_killed and menu.get_buttons():
            for button in menu.get_buttons():
                if button.pos[0] < mouse_weight < button.get_left_pos()[0] and button.pos[1] < mouse_height < \
                        button.get_left_pos()[1]:
                    if not button.is_focus:
                        Event(button, button.focused)
                else:
                    if button.is_focus:
                        Event(button, button.dis_focus)


def is_mouse_press(mouse_weight, mouse_height):
    for menu in get_active_screen():
        if not menu.is_killed and menu.get_buttons():
            for button in menu.get_buttons():
                if button.pos[0] < mouse_weight < button.get_left_pos()[0] and button.pos[1] < mouse_height < \
                        button.get_left_pos()[1]:
                    Event(button, button.clicked)


def is_key_press(event):
    for menu in get_active_screen():
        if not menu.is_killed and menu.get_input_boxs():
            for input_box in menu.get_input_boxs():
                input_box.handle_event(event)


def is_key_press_in_game(event, game):
    ang_vel = 4.5
    if event.key == pygame.K_LEFT:
        game.ship.set_angle_vel(ang_vel)
    if event.key == pygame.K_RIGHT:
        game.ship.set_angle_vel(-ang_vel)
    if event.key == pygame.K_UP:
        game.ship.set_thrust(True)
    if event.key == pygame.K_SPACE:
        game.ship.shoot()


def is_key_un_press_in_game(event, game):
    if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
        game.ship.set_angle_vel(0)
    if event.key == pygame.K_UP:
        game.ship.set_thrust(False)
