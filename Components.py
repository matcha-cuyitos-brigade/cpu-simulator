import time


class IntegratedCircuit:

    def __init__(self):
        self.manufacturer = ''
        self.build_date = ''
        self.purpose = ''

    def __init__(self, manufacturer, build_date, purpose):
        self.manufacturer = manufacturer
        self.build_date = build_date
        self.purpose = purpose


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


class CU(IntegratedCircuit):

    def __init__(self, clock):
        IntegratedCircuit.__init__(self)
        self.instruction_address_register = 0  # also known as program counter (PC)
        self.opcode, self.operand_1, self.operand_2 = 0
        self.instruction_register = [self.opcode, self.operand_1, self.operand_2]
        self.purpose = "The control unit (CU) is a component of a computer's central processing unit (CPU) that " \
                       "directs the operation of the processor. It tells the computer's memory, arithmetic and logic " \
                       "unit and input and output devices how to respond to the instructions that have been sent to " \
                       "the processor."
        self.clock = clock

    @staticmethod
    def fetch():
        assembly_line = 0
        return assembly_line

    def decode(self, assembly_line):
        return self.opcode, self.operand_1, self.operand_2

    def execute(self):
        return

    def instruction_cycle(self):
        if self.clock == -1:
            assembly_line = self.fetch()
            self.opcode, self.operand_1, self.operand_2 = self.decode(assembly_line)
            self.execute()
        elif self.clock == 0:
            input("[Debug mode] Press Enter to continue...")
            assembly_line = self.fetch()
            input("[Debug mode] Press Enter to continue...")
            self.opcode, self.operand_1, self.operand_2 = self.decode(assembly_line)
            input("[Debug mode] Press Enter to continue...")
            self.execute()
        else:
            time.sleep(1 / self.clock)
            assembly_line = self.fetch()
            time.sleep(1 / self.clock)
            self.opcode, self.operand_1, self.operand_2 = self.decode(assembly_line)
            time.sleep(1 / self.clock)
            self.execute()
        self.instruction_address_register += 1


class CPU:
    def __init__(self, clock):
        alu = ALU()
        cu = CU(clock)
        register_a = 0
        register_b = 0
        register_c = 0
        register_d = 0


class RAM:
    def __init__(self, ram_array):
        self.ram_array = ram_array
