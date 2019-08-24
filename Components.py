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
        self.instruction_register = [0, 0]  # opcode / param
        self.purpose = "The control unit (CU) is a component of a computer's central processing unit (CPU) that " \
                       "directs the operation of the processor. It tells the computer's memory, arithmetic and logic " \
                       "unit and input and output devices how to respond to the instructions that have been sent to " \
                       "the processor."
        self.clock = clock

    @staticmethod
    def fetch(self):
        return 1

    def instruction_cycle(self):
        if self.clock == -1:
            self.fetch()
            self.decode()
            self.execute()
        elif self.clock == 0:
            input("[Debug mode] Press Enter to continue...")
            self.fetch()
            input("[Debug mode] Press Enter to continue...")
            self.decode()
            input("[Debug mode] Press Enter to continue...")
            self.execute()
        else:
            time.sleep(1 / self.clock)
            self.fetch()
            time.sleep(1 / self.clock)
            self.decode()
            time.sleep(1 / self.clock)
            self.execute()




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
