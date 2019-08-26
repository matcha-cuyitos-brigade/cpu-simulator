from Components.IntegratedCircuit import *
import Interpreter
import time


class CU(IntegratedCircuit):

    def __init__(self, clock):
        self._instruction_address_register = 0  # also known as program counter (PC)
        self._opcode = 0
        self._operand_1 = 0
        self._operand_2 = 0
        self._instruction_register = [self._opcode, self._operand_1, self._operand_2]
        self._clock = clock
        IntegratedCircuit.__init__(self)
        self.purpose = "The control unit (CU) is a component of a computer's central processing unit (CPU) that " \
                       "directs the operation of the processor. It tells the computer's memory, arithmetic and logic " \
                       "unit and input and output devices how to respond to the instructions that have been sent to " \
                       "the processor."

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
        print("  CU:  ", self.__dict__)

    # -----------------------------------------------------------------------------------------------------------

    def fetch(self):
        assembly_line = Interpreter.get_assembly_line.__func__(self.instruction_address_register)
        print("\n", assembly_line)
        return assembly_line

    def decode(self, assembly_line):
        self.opcode, self.operand_1, self.operand_2 = Interpreter.get_instruction_register.__func__(assembly_line)

    def execute(self, ram, cpu):
        if self.opcode == 0:  # output
            cpu.alu.output = ram.ram_array[self.operand_1]
            self.instruction_address_register += 1

        elif self.opcode == 1:  # load_a
            cpu.register_a = ram.ram_array[self.operand_1]
            self.instruction_address_register += 1

        elif self.opcode == 2:  # load_b
            cpu.register_b = ram.ram_array[self.operand_1]
            self.instruction_address_register += 1

        elif self.opcode in [3, 7]:  # and, or
            if self.operand_1 in ["A", "a"]:
                self.operand_1 = cpu.register_a
            elif self.operand_1 in ["B", "b"]:
                self.operand_1 = cpu.register_b
            elif self.operand_1 in ["C", "c"]:
                self.operand_1 = cpu.register_c
            elif self.operand_1 in ["D", "d"]:
                self.operand_1 = cpu.register_d

            if self.operand_2 in ["A", "a"]:
                self.operand_2 = cpu.register_a
            elif self.operand_2 in ["B", "b"]:
                self.operand_2 = cpu.register_b
            elif self.operand_2 in ["C", "c"]:
                self.operand_2 = cpu.register_c
            elif self.operand_2 in ["D", "d"]:
                self.operand_2 = cpu.register_d
            cpu.alu.calc(self.operand_1, self.operand_2, self.opcode)
            self.instruction_address_register += 1

        elif self.opcode == 4:  # immediate_read_a
            cpu.register_a = self.operand_1
            self.instruction_address_register += 1

        elif self.opcode == 5:  # store_a
            ram.ram_array[self.operand_1] = cpu.register_a
            self.instruction_address_register += 1

        elif self.opcode == 6:  # store_b
            ram.ram_array[self.operand_1] = cpu.register_b
            self.instruction_address_register += 1

        elif self.opcode == 8:  # immediate_read_b
            cpu.register_b = self.operand_1
            self.instruction_address_register += 1

        elif self.opcode in [9, 10]:  # add, sub
            if self.operand_1 in ["A", "a"]:
                self.operand_1 = cpu.register_a
            elif self.operand_1 in ["B", "b"]:
                self.operand_1 = cpu.register_b
            elif self.operand_1 in ["C", "c"]:
                self.operand_1 = cpu.register_c
            elif self.operand_1 in ["D", "d"]:
                self.operand_1 = cpu.register_d

            if self.operand_2 in ["A", "a"]:
                self.operand_2 = cpu.register_a
                cpu.alu.calc(self.operand_1, self.operand_2, self.opcode)
                cpu.register_a = cpu.alu.output
            elif self.operand_2 in ["B", "b"]:
                self.operand_2 = cpu.register_b
                cpu.alu.calc(self.operand_1, self.operand_2, self.opcode)
                cpu.register_b = cpu.alu.output
            elif self.operand_2 in ["C", "c"]:
                self.operand_2 = cpu.register_c
                cpu.alu.calc(self.operand_1, self.operand_2, self.opcode)
                cpu.register_c = cpu.alu.output
            elif self.operand_2 in ["D", "d"]:
                self.operand_2 = cpu.register_d
                cpu.alu.calc(self.operand_1, self.operand_2, self.opcode)
                cpu.register_d = cpu.alu.output
            self.instruction_address_register += 1

        elif self.opcode == 11:  # jump
            self.instruction_address_register = self.operand_1

        elif self.opcode == 12:  # jump_neg
            if cpu.alu.flag_negative == 1:
                self.instruction_address_register = self.operand_1

        elif self.opcode == 13:  # load_c
            cpu.register_c = ram.ram_array[self.operand_1]
            self.instruction_address_register += 1

        elif self.opcode == 14:  # store_d
            ram.ram_array[self.operand_1] = cpu.register_d
            self.instruction_address_register += 1

    def instruction_cycle(self, ram, cpu):
        if self.clock == -1:
            assembly_line = self.fetch()
            self.decode(assembly_line)
            self.execute(ram, cpu)
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
            self.execute(ram, cpu)

# mycu = CU(0)
# print(mycu.fetch())
# mycu.print_status()
# mycu.decode(mycu.fetch())
# mycu.print_status()
