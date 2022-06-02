from utils import angle_to_vector


class Ship:
    def __init__(self, pos, vel, angle, image, thrust_image, info):
        self.pos = [pos[0] - 45, pos[1] - 45]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.thrust_image = thrust_image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.forward = [0, 0]

    def shoot(self):
        missile_pos = [self.pos[0] + 40 + self.radius * self.forward[0],
                       self.pos[1] + 40 + self.radius * self.forward[1]]

        missile_vel = [self.vel[0] + 6 * self.forward[0], self.vel[1] + 6 * self.forward[1]]
        missile_group.add(Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info, missile_sound))

    def set_thrust(self, thrust):
        self.thrust = thrust
        if thrust:
            thruster_sound.play()
        else:
            thruster_sound.stop()

    def get_position(self):
        return int(self.pos[0] + self.radius), int(self.pos[1] + self.radius)

    def get_radius(self):
        return self.radius

    def draw(self, canvas):
        if self.thrust:
            canvas.blit(rot_center(self.thrust_image, self.angle), self.pos)
        else:
            canvas.blit(rot_center(self.image, self.angle), self.pos)

    def update(self):
        acc = 0.5
        fric = acc / 20
        self.angle += self.angle_vel
        self.forward = angle_to_vector(math.radians(self.angle))
        if self.thrust:
            self.vel[0] += self.forward[0] * acc
            self.vel[1] += self.forward[1] * acc
        self.vel[0] *= (1 - fric)
        self.vel[1] *= (1 - fric)
        self.pos[0] = (self.pos[0] + self.vel[0]) % (WIDTH - self.radius)
        self.pos[1] = (self.pos[1] + self.vel[1]) % (HEIGHT - self.radius)

    def set_angle_vel(self, vel):
        self.angle_vel = vel
