from object.animations import Animation

animates = []


class Event:
    def __init__(self, item, event):
        event()
        if item.animator is not None and item.animator.animation.get_animation(event) is not None:
            item.animator.start_animate(event)


class Animator:
    def __init__(self, animation: Animation):
        self.animation = animation

    def start_animate(self, event):
        animates.append(self.animation)


def animate_all():
    for a in animates:
        a.animate()
