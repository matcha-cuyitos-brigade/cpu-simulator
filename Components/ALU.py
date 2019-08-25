from Components import IntegratedCircuit


class ALU(IntegratedCircuit):

    def __init__(self):
        IntegratedCircuit.__init__(self)
        self.input_a = 0
        self.input_b = 0
        self.opcode = 0
        self.output = 0
        self.flag_overflow = 0
        self.flag_zero = 0
        self.flag_negative = 0
        self.purpose = "An arithmetic logic unit (ALU) is a digital circuit used to perform arithmetic and logic " \
                       "operations. It represents the fundamental building block of the central processing unit (CPU) " \
                       "of a computer. "

    def calc_and(self):
        0

    def calc_or(self):
        0

    def calc_add(self):
        0

    def calc_sub(self):
        0

    @property
    def input_a(self):
        return self._input_a