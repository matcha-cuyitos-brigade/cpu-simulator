from Components import IntegratedCircuit
import Interpreter
import time


class CU(IntegratedCircuit):

    def __init__(self, clock):
        IntegratedCircuit.__init__(self)
        self.instruction_address_register = 0  # also known as program counter (PC)
        self.opcode = 0
        self.operand_1 = 0
        self.operand_2 = 0
        self.instruction_register = [self.opcode, self.operand_1, self.operand_2]
        self.purpose = "The control unit (CU) is a component of a computer's central processing unit (CPU) that " \
                       "directs the operation of the processor. It tells the computer's memory, arithmetic and logic " \
                       "unit and input and output devices how to respond to the instructions that have been sent to " \
                       "the processor."
        self.clock = clock

    def fetch(self):
        assembly_line = Interpreter.get_assembly_line.__func__(self.instruction_address_register)
        return assembly_line

    def decode(self, assembly_line):
        self.opcode, self.operand_1, self.operand_2 = Interpreter.get_instruction_register.__func__(assembly_line)

    def execute(self, alu, ram, register_a, register_b, register_c, register_d):
        if self.opcode == 0:
            alu.output = ram.ram_array[self.operand_1]
            print(alu.output)
            self.instruction_address_register += 1

        elif self.opcode == 1:
            register_a = ram.ram_array[self.operand_1]
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

    def instruction_cycle(self, alu, ram, register_a, register_b, register_c, register_d):
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
            self.execute(alu, ram, register_a, register_b, register_c, register_d)
        else:
            time.sleep(1 / self.clock)
            assembly_line = self.fetch()
            time.sleep(1 / self.clock)
            self.opcode, self.operand_1, self.operand_2 = self.decode(assembly_line)
            time.sleep(1 / self.clock)
            self.execute()
        # self.instruction_address_register += 1