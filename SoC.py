from Components.CPU import *
from Components.RAM import *
import re


class SoC:
    def __init__(self):
        self._cpu = CPU(0)
        self._ram = RAM([6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6])

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
        bios = open("bios.yml", "r")
        list_of_bios_lines = bios.readlines()
        self.cpu.cu.clock = float(re.search(r"[-]?[0-9]*\.?,?[0-9]+", list_of_bios_lines[2]).group())

        j = 0
        for i in range(13, 29):
            self.ram.ram_array[j] = re.search(r"\d+(\.\d{0,9})?", list_of_bios_lines[i]).group()
            j += 1
        return "true" in list_of_bios_lines[6], "true" in list_of_bios_lines[7],\
               "true" in list_of_bios_lines[8], "true" in list_of_bios_lines[9]

    def run(self):
        while self.cpu.cu.opcode != 15:
            self.cpu.cu.instruction_cycle(self.ram, self.cpu)


mysoc = SoC()
mysoc.cpu.print_status()
mysoc.ram.print_status()
print(mysoc.boot())
mysoc.run()
mysoc.cpu.print_status()
mysoc.ram.print_status()
