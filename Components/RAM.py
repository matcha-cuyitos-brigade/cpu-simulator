class RAM:
    def __init__(self, ram_array):
        self._ram_array = ram_array

    @property
    def ram_array(self):
        return self._ram_array

    @ram_array.setter
    def ram_array(self, val):
        self._ram_array = val

    def get_status(self):
        return self.__dict__

    def print_status(self):
        print("RAM: ", self.__dict__)
