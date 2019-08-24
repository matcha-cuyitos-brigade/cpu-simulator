import re


@staticmethod
def get_assembly_line(instruction_address_register):
    assembly_code = open(r".code/ex1.code", "r")
    list_of_lines = assembly_code.readlines()
    print(list_of_lines)

    list_filtered = [x for x in list_of_lines if "#" not in x]
    print(list_filtered)
    return list_filtered[instruction_address_register]


@staticmethod
def get_instruction_register(assembly_line):
    if re.search("(OUTPUT)", assembly_line) or re.search("(0000)", assembly_line):
        print("SÍ")
    elif re.search("(LOAD_A)", assembly_line) or re.search("(0001)", assembly_line):
        print("SÍ")
    elif re.search("(LOAD_B)", assembly_line) or re.search("(0010)", assembly_line):
        print("SÍ")
    elif re.search("(AND)", assembly_line) or re.search("(0011)", assembly_line):
        print("SÍ")
    elif re.search("(ILD_A)", assembly_line) or re.search("(0100)", assembly_line):
        print("SÍ")
    elif re.search("(STORE_A)", assembly_line) or re.search("(0101)", assembly_line):
        print("SÍ")
    elif re.search("(STORE_B)", assembly_line) or re.search("(0110)", assembly_line):
        print("SÍ")
    elif re.search("(OR)", assembly_line) or re.search("(0111)", assembly_line):
        print("SÍ")
    elif re.search("(ILD_B)", assembly_line) or re.search("(1000)", assembly_line):
        print("SÍ")
    elif re.search("(ADD)", assembly_line) or re.search("(1001)", assembly_line):
        print("SÍ")
    elif re.search("(SUB)", assembly_line) or re.search("(1010)", assembly_line):
        print("SÍ")
    elif re.search("(JUMP)", assembly_line) or re.search("(1011)", assembly_line):
        print("SÍ")
    elif re.search("(JUMP_NEG)", assembly_line) or re.search("(1100)", assembly_line):
        print("SÍ")
    elif re.search("(LOAD_C)", assembly_line) or re.search("(1101)", assembly_line):
        print("SÍ")
    elif re.search("(STORE_D)", assembly_line) or re.search("(1110)", assembly_line):
        print("SÍ")
    elif re.search("(HALT)", assembly_line) or re.search("(1111)", assembly_line):
        print("SÍ")


get_instruction_register.__func__("OUTPUT A\n")
