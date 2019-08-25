from Components.ALU import *
from Components.CU import *


class CPU:
    def __init__(self, clock):
        self._alu = ALU()
        self._cu = CU(clock)
        self._register_a = 0
        self._register_b = 0
        self._register_c = 0
        self._register_d = 0

    @property
    def alu(self):
        return self._alu

    @property
    def cu(self):
        return self._cu

    @property
    def register_a(self):
        return self._register_a

    @register_a.setter
    def register_a(self, val):
        self._register_a = val

    @property
    def register_b(self):
        return self._register_b

    @register_b.setter
    def register_b(self, val):
        self._register_b = val

    @property
    def register_c(self):
        return self._register_c

    @register_c.setter
    def register_c(self, val):
        self._register_c = val

    @property
    def register_d(self):
        return self._register_d

    @register_d.setter
    def register_d(self, val):
        self._register_d = val

    def get_status(self):
        return self.__dict__

    def print_status(self):
        print(self.__dict__)
