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

    def __init__(self):
        IntegratedCircuit.__init__(self)
        self.instruction_address_register = 0
        self.instruction_register = [0, 0]  # opcode / param
        self.purpose = "The control unit (CU) is a component of a computer's central processing unit (CPU) that " \
                       "directs the operation of the processor. It tells the computer's memory, arithmetic and logic " \
                       "unit and input and output devices how to respond to the instructions that have been sent to " \
                       "the processor. "
