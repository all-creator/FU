import math
import pygame
import random

from system.object.background import DynamicBackgroundItem
from system.enums import bg_item
from gui.object.animations import Scale
from gui.object.menu import Img


def gen_dynamic_bg(bg, screen):
    for h in range(screen.get_height() // 100):
        bg.items.append(DynamicBackgroundItem(bg_item, vector=[5, 5],
                                              pos=[h * 200, 200 * random.random()], scale_size=[70, 70]))
    for w in range(1, screen.get_width() // 100):
        bg.items.append(DynamicBackgroundItem(bg_item, vector=[5, 5],
                                              pos=[0, w * 200], scale_size=[70, 70]))
    for i in range(4):
        for d in range(screen.get_height() // 200):
            bg.items.append(DynamicBackgroundItem(
                bg_item, vector=[i + 4, i + 4], pos=[d * 100 * round(10 * random.random()), (200 + i * 100) *
                                                     random.random() * round(10 * random.random())], scale_size=[70, 70]))


def rotate_center(image: pygame.Surface, angle):
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    try:
        rot_image = rot_image.subsurface(rot_rect).copy()
    except ValueError:
        pass
    return rot_image


def load_img(img, size=1):
    img = Img(img)
    scale = Scale(img, size)
    scale.active()
    return scale.item.item


def group_collide(group, other_object):
    counter = len(group)

    for element in list(group):
        if element.collide(other_object):
            group.remove(element)

    return counter - len(group)


def group_group_collide(first_group, second_group):
    counter = 0

    for element in list(first_group):
        if group_collide(second_group, element) > 0:
            counter += 1
            first_group.remove(element)

    return counter


def angle_to_vector(ang):
    return [math.cos(ang), - math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
