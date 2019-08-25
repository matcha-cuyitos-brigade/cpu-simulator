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
        operand_1 = re.search("[1][0-6]|[1-9]", assembly_line).group()
        return 0, int(operand_1), 0
    elif re.search("(LOAD_A)", assembly_line) or re.search("(0001)", assembly_line):
        operand_1 = re.search("[1][0-6]|[1-9]", assembly_line).group()
        return 1, int(operand_1), 0
    elif re.search("(LOAD_B)", assembly_line) or re.search("(0010)", assembly_line):
        operand_1 = re.search("[1][0-6]|[1-9]", assembly_line).group()
        return 2, int(operand_1), 0
    elif re.search("(AND)", assembly_line) or re.search("(0011)", assembly_line):
        assembly_line = re.split("\s", assembly_line)
        return 3, assembly_line[1], assembly_line[2]
    elif re.search("(ILD_A)", assembly_line) or re.search("(0100)", assembly_line): #immediate load
        assembly_line = re.split("\s", assembly_line)
        return 4, int(assembly_line[1]), 0
    elif re.search("(STORE_A)", assembly_line) or re.search("(0101)", assembly_line):
        assembly_line = re.split("\s", assembly_line)
        return 5, int(assembly_line[1]), 0
    elif re.search("(STORE_B)", assembly_line) or re.search("(0110)", assembly_line):
        assembly_line = re.split("\s", assembly_line)
        return 6, int(assembly_line[1]), 0
    elif re.search("(OR)", assembly_line) or re.search("(0111)", assembly_line):
        assembly_line = re.split("\s", assembly_line)
        return 7, assembly_line[1], assembly_line[2]
    elif re.search("(ILD_B)", assembly_line) or re.search("(1000)", assembly_line):
        assembly_line = re.split("\s", assembly_line)
        return 8, int(assembly_line[1]), 0
    elif re.search("(ADD)", assembly_line) or re.search("(1001)", assembly_line):
        assembly_line = re.split("\s", assembly_line)
        return 9, assembly_line[1], assembly_line[2]
    elif re.search("(SUB)", assembly_line) or re.search("(1010)", assembly_line):
        assembly_line = re.split("\s", assembly_line)
        return 10, assembly_line[1], assembly_line[2]
    elif re.search("(JUMP)", assembly_line) or re.search("(1011)", assembly_line):
        assembly_line = re.split("\s", assembly_line)
        return 11, int(assembly_line[1]), 0
    elif re.search("(JUMP_NEG)", assembly_line) or re.search("(1100)", assembly_line):
        assembly_line = re.split("\s", assembly_line)
        return 12, int(assembly_line[1]), 0
    elif re.search("(LOAD_C)", assembly_line) or re.search("(1101)", assembly_line):
        operand_1 = re.search("[1][0-6]|[1-9]", assembly_line).group()
        return 13, int(operand_1), 0
    elif re.search("(STORE_D)", assembly_line) or re.search("(1110)", assembly_line):
        assembly_line = re.split("\s", assembly_line)
        return 14, int(assembly_line[1]), 0
    elif re.search("(HALT)", assembly_line) or re.search("(1111)", assembly_line):
        return 15, 0, 0


#get_instruction_register.__func__("AND A B\n")
