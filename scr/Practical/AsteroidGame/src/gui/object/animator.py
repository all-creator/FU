
animates = []

SPAWN = 'is_load'
IS_FOCUS = 'focused'
DIS_FOCUS = 'dis_focus'
CLICKED = 'clicked'
KILLED = 'kill'


class Event:
    def __init__(self, item, event):
        event()
        if item.animator.get_animation(event) is not None:
            item.animator.start_animate(event)


class Animator:
    def __init__(self, item):
        self.item = item
        self.animations = {}

    def bind(self, anim, event):
        self.animations.setdefault(self.item.__getattribute__(event), anim)

    def get_animation(self, event):
        return self.animations.get(event)

    def start_animate(self, event):
        self.get_animation(event).animate()


def animate_all():
    for a in animates:
        a.animate()
