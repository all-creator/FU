class Animation:
    def __init__(self, item):
        self.item = item
        self.animations = {}

    def bind(self, anim, event):
        self.animations.setdefault(self.item.__getattribute__(event), anim)

    def get_animation(self, event):
        return self.animations.get(event)

