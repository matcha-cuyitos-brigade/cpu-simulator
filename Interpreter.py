
@staticmethod
def get_assembly_line(instruction_address_register):
    assembly_code = open(r".code/ex1.code", "r")
    list_of_lines = assembly_code.readlines()
    print(list_of_lines)

    list_filtered = [x for x in list_of_lines if "#" not in x]
    print(list_filtered)
    return list_filtered[instruction_address_register]
