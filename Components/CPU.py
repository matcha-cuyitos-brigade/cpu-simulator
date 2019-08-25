class CPU:
    def __init__(self, clock):
        self.alu = ALU()
        self.cu = CU(clock)
        self.register_a = 0
        self.register_b = 0
        self.register_c = 0
        self.register_d = 0