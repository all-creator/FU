import pygame

from game.utils import dist, rotate_center, load_img
from system.object.display import get_default_screen
from system.enums import sound, screen
from pygame.sprite import Sprite


class ImgMeta:
    def __init__(self, center, size, radius=0, lifespan=None, animated=False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


class GameObj:
    def __init__(self, pos, vel, ang, ang_vel, image, info, _sound=None):
        super().__init__()
        if _sound:
            _sound.play()
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        self.pos = [pos[0] + self.radius, pos[1] + self.radius]

    def collide(self, other_object):
        if dist(self.pos, other_object.get_position()) <= self.radius + other_object.get_radius():
            return True
        else:
            return False

    def get_position(self):
        return [int(self.pos[0]), int(self.pos[1])]

    def get_radius(self):
        return self.radius

    def render(self, canvas):
        if self.lifespan > self.age:
            if self.animated:
                self.age += 1
                if self.age < self.lifespan:
                    canvas.blit(self.image[self.age], self.pos)
            else:
                canvas.blit(rotate_center(self.image, self.angle),
                            (int(self.pos[0] - self.radius), int(self.pos[1] - self.radius)))
        else:
            del self

    def update(self):
        if self.lifespan > self.age:
            self.angle += self.angle_vel
            self.pos[0] = (self.pos[0] + self.vel[1]) % get_default_screen().get_width()
            self.pos[1] = (self.pos[1] - self.vel[0]) % get_default_screen().get_height()
            self.age += 1


class Missile(GameObj):
    def __init__(self, pos, vel, ang, ang_vel):
        img: pygame.Surface = load_img("../res/game/missile.png", 0.2)
        w = img.get_width()
        h = img.get_height()
        super().__init__(pos, vel, ang, ang_vel, img, ImgMeta([w/2, h/2], [w, h], int((w/2 + h/2)/2),
                                                              screen.get_height() // 40 + screen.get_width() // 60),
                         _sound=sound.get_missile_sound())


class Asteroid(GameObj):
    def __init__(self, pos, vel, ang, ang_vel):
        img: pygame.Surface = load_img("../res/game/asteroid_sprite.png", 0.3)
        w = img.get_width()
        h = img.get_height()
        super().__init__(pos, vel, ang, ang_vel, img, ImgMeta([w/2, h/2], [w, h], int((w/2 + h/2)/2)),
                         _sound=sound.get_missile_sound())
