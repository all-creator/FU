import time
from threading import Thread

from system.utils.time_utils import current_milli_time


class Scheduler:
    def __init__(self, process, delay=0, rep=0, *args):
        self.process = Thread(target=process, args=args)
        self.delay = delay
        self.rep = rep
        self.is_kill = False
        self.c_time = current_milli_time()

    def run(self):
        if self.delay:
            time.sleep(self.delay / 1000)
            self.c_time = current_milli_time()
        self.process.start()
        while self.rep and not self.is_kill:
            if current_milli_time() >= self.c_time + self.rep:
                self.process.start()
                self.c_time = current_milli_time()

    def kill(self):
        self.is_kill = True


class Pool:
    def __init__(self):
        self.process = []

    def start(self):
        for p in self.process:
            p.run()

    def add(self, process: Scheduler):
        self.process.append(process)

    def kill(self):
        for p in self.process:
            p.kill()
