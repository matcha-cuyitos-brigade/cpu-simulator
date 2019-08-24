import Components as c

class SoC:
    def __init__(self, clock, ram_array):
        self.cpu = c.CPU(clock)
        self.ram = c.RAM(ram_array)




