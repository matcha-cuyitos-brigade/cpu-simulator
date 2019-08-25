from Components.IntegratedCircuit import *


class ALU(IntegratedCircuit):

    def __init__(self):
        self._input_a = 0
        self._input_b = 0
        self._opcode = 0
        self._output = 0
        self._flag_overflow = 0
        self._flag_zero = 0
        self._flag_negative = 0
        IntegratedCircuit.__init__(self)
        self._purpose = "An arithmetic logic unit (ALU) is a digital circuit used to perform arithmetic and logic " \
                        "operations. It represents the fundamental building block of the central processing unit " \
                        "(CPU) of a computer. "

    def calc_and(self):
        return self.input_a & self.input_b

    def calc_or(self):
        return self.input_a | self.input_b

    def calc_add(self):
        return self.input_a + self.input_b

    def calc_sub(self):
        return self.input_a - self.input_b

    def calc(self, input_a, input_b, opcode):
        self.input_a = input_a
        self.input_b = input_b
        self.opcode = opcode

        if opcode == 3:
            self.output = self.calc_and()
        elif opcode == 7:
            self.output = self.calc_or()
        elif opcode == 9:
            self.output = self.calc_add()
        elif opcode == 10:
            self.output = self.calc_sub()

        if self.output == 0:
            self.flag_zero = 1
        elif self.output < 0:
            self.flag_negative = 1
        elif self.output > 15:
            self.flag_overflow = 1

    @property
    def input_a(self):
        return self._input_a

    @input_a.setter
    def input_a(self, val):
        self._input_a = int(val)

    @property
    def input_b(self):
        return self._input_b

    @input_b.setter
    def input_b(self, val):
        self._input_b = int(val)

    @property
    def opcode(self):
        return self._opcode

    @opcode.setter
    def opcode(self, val):
        self._opcode = val

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, val):
        self._output = abs(int(val))
        print("Output: ", val)

    @property
    def flag_overflow(self):
        return self._flag_overflow

    @flag_overflow.setter
    def flag_overflow(self, val):
        self._flag_overflow = val

    @property
    def flag_zero(self):
        return self._flag_zero

    @flag_zero.setter
    def flag_zero(self, val):
        self._flag_zero = val

    @property
    def flag_negative(self):
        return self._flag_negative

    @flag_negative.setter
    def flag_negative(self, val):
        self._flag_negative = val

    def get_status(self):
        return self.__dict__

    def print_status(self):
        print("  ALU: ", self.__dict__)


# myalu = ALU()
# print(myalu.__dict__)
# myalu.calc(3, 3, 9)
# print(myalu.__dict__)
# print(myalu.get_status())
