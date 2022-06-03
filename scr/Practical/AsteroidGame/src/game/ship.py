from game.utils import angle_to_vector, rotate_center
from system.object.display import get_default_screen
from game.game_object import Missile
from system.enums import sound

import math


class Ship:
    def __init__(self, pos, vel, image, active_image, info, angle=0, missile_group=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.active = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.active_image = active_image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.forward = [0, 0]
        self.missile_group = missile_group

    def shoot(self):
        missile_pos = [self.pos[0] + self.radius * self.forward[0],
                       self.pos[1] + self.radius * self.forward[1]]

        missile_vel = [self.vel[0] + 6 * self.forward[0], self.vel[1] + 6 * self.forward[1]]
        self.missile_group.add(Missile(missile_pos, missile_vel, self.angle, 0))

    def set_thrust(self, thrust):
        self.active = thrust
        if sound.get_active_ship_sound():
            if thrust:
                sound.get_active_ship_sound().play()
            else:
                sound.get_active_ship_sound().stop()

    def get_position(self):
        return int(self.pos[0] + self.radius), int(self.pos[1] + self.radius)

    def get_radius(self):
        return self.radius

    def render(self, screen):
        if self.active:
            screen.blit(rotate_center(self.active_image, self.angle), self.pos)
        else:
            screen.blit(rotate_center(self.image, self.angle), self.pos)

    def update(self):
        acc = 0.5
        fc = acc / 20
        self.angle += self.angle_vel
        self.forward = angle_to_vector(math.radians(self.angle))
        if self.active:
            self.vel[0] += self.forward[1] * acc
            self.vel[1] -= self.forward[0] * acc
        self.vel[0] *= (1 - fc)
        self.vel[1] *= (1 - fc)
        self.pos[0] = (self.pos[0] + self.vel[0]) % (get_default_screen().get_width() - self.radius)
        self.pos[1] = (self.pos[1] + self.vel[1]) % (get_default_screen().get_height() - self.radius)

    def set_angle_vel(self, vel):
        self.angle_vel = vel
