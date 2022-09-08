
class Function:

    def __init__(self, func, args=None):
        self.func = func
        self.args = args

    def run(self):
        if self.args:
            self.func(self.args)
        else:
            self.func()
