from Components.IntegratedCircuit import *
import Interpreter
import time


class CU(IntegratedCircuit):

    def __init__(self, clock):
        IntegratedCircuit.__init__(self)
        self._instruction_address_register = 0  # also known as program counter (PC)
        self._opcode = 0
        self._operand_1 = 0
        self._operand_2 = 0
        self._instruction_register = [self._opcode, self._operand_1, self._operand_2]
        self.purpose = "The control unit (CU) is a component of a computer's central processing unit (CPU) that " \
                       "directs the operation of the processor. It tells the computer's memory, arithmetic and logic " \
                       "unit and input and output devices how to respond to the instructions that have been sent to " \
                       "the processor."
        self._clock = clock

    @property
    def instruction_address_register(self):
        return self._instruction_address_register

    @instruction_address_register.setter
    def instruction_address_register(self, val):
        self._instruction_address_register = val

    @property
    def opcode(self):
        return self._opcode

    @opcode.setter
    def opcode(self, val):
        self._opcode = val

    @property
    def operand_1(self):
        return self._operand_1

    @operand_1.setter
    def operand_1(self, val):
        self._operand_1 = val

    @property
    def operand_2(self):
        return self._operand_2

    @operand_2.setter
    def operand_2(self, val):
        self._operand_2 = val

    @property
    def instruction_register(self):
        return self._instruction_register

    @instruction_register.setter
    def instruction_register(self, val):
        self._instruction_register = val

    @property
    def clock(self):
        return self._clock

    @clock.setter
    def clock(self, val):
        self._clock = val

    def get_status(self):
        return self.__dict__

    def print_status(self):
        print(self.__dict__)

    # -----------------------------------------------------------------------------------------------------------

    def fetch(self):
        assembly_line = Interpreter.get_assembly_line.__func__(self.instruction_address_register)
        return assembly_line

    def decode(self, assembly_line):
        self.opcode, self.operand_1, self.operand_2 = Interpreter.get_instruction_register.__func__(assembly_line)

    def execute(self, ram, cpu):
        if self.opcode == 0:
            0
            #cpu.alu.output = ram.ram_array[self.operand_1]
            #print(alu.output)
            #self.instruction_address_register += 1

        elif self.opcode == 1:
            cpu.register_a = ram.ram_array[self.operand_1]
            self.instruction_address_register += 1

        elif self.opcode == 2:
            0
        elif self.opcode == 3:
            0
        elif self.opcode == 4:
            0
        elif self.opcode == 5:
            0
        elif self.opcode == 6:
            0
        elif self.opcode == 7:
            0
        elif self.opcode == 8:
            0
        elif self.opcode == 9:
            0
        elif self.opcode == 10:
            0
        elif self.opcode == 11:
            0
        elif self.opcode == 12:
            0
        elif self.opcode == 13:
            0
        elif self.opcode == 14:
            0
        elif self.opcode == 15:
            0
        return

    def instruction_cycle(self, ram, cpu):
        if self.clock == -1:
            assembly_line = self.fetch()
            self.decode(assembly_line)
            self.execute()
        elif self.clock == 0:
            input("[Debug mode] Press Enter to continue...")
            assembly_line = self.fetch()
            input("[Debug mode] Press Enter to continue...")
            self.decode(assembly_line)
            input("[Debug mode] Press Enter to continue...")
            self.execute(ram, cpu)
        else:
            time.sleep(1 / self.clock)
            assembly_line = self.fetch()
            time.sleep(1 / self.clock)
            self.decode(assembly_line)
            time.sleep(1 / self.clock)
            self.execute()


# mycu = CU(0)
# print(mycu.fetch())
# mycu.print_status()
# mycu.decode(mycu.fetch())
# mycu.print_status()