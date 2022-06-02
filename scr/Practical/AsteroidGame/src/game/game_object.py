from utils import dist
from system.object.display import get_default_screen


class GameObj:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        if sound:
            sound.play()
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

    def draw(self, canvas):

        if self.animated:
            self.age += 1
            if self.age < self.lifespan:
                canvas.blit(self.image[self.age], self.pos)
        else:
            canvas.blit(rot_center(self.image, self.angle),
                        (int(self.pos[0] - self.radius), int(self.pos[1] - self.radius)))

    def update(self):
        self.angle += self.angle_vel
        self.pos[0] = (self.pos[0] + self.vel[0]) % get_default_screen().get_width()
        self.pos[1] = (self.pos[1] + self.vel[1]) % get_default_screen().get_height()
        self.age += 1
        if self.age < self.lifespan:
            return False
        else:
            return True
