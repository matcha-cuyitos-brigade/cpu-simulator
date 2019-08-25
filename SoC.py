from Components.CPU import *
from Components.RAM import *


class SoC:
    def __init__(self):
        self._cpu = CPU(0)
        self._ram = RAM([6, 6, 0, 0, 0, 0, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6])

    @property
    def cpu(self):
        return self._cpu

    @cpu.setter
    def cpu(self, val):
        self._cpu = val

    @property
    def ram(self):
        return self._ram

    @ram.setter
    def ram(self, val):
        self._ram = val

    def get_status(self):
        return self.__dict__

    def print_status(self):
        print(self.__dict__)

    def boot(self):
        0

    def run(self):
        self.cpu.cu.instruction_cycle(self.ram, self.cpu)

mysoc = SoC()
mysoc.cpu.print_status()
mysoc.run()
mysoc.cpu.print_status()