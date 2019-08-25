from Components import RAM as c


class SoC:
    def __init__(self):
        self.cpu = c.CPU(0)
        self.ram = c.RAM([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def boot(self):
        0

    def run(self):
        self.cpu.cu.instruction_cycle(self.cpu.alu, self.ram, self.cpu.register_a, self.cpu.register_b, self.cpu.register_c, self.cpu.register_d)

mysoc = SoC()
mysoc.run()
