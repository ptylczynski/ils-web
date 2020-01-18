import os
from threading import Thread

from ils_web.settings import BASE_DIR
from maths.simulator import Simulator


class AsyncSimulatorWrapper(Thread):
    def __init__(self, callable: Simulator):
        self.callable: Simulator = callable
        super().__init__()

    def run(self):
        self.callable.simulate()
        with open(BASE_DIR + "/plots/lock", "w") as file:
            file.write("s")
