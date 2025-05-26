class Conversor:
    def __init__(self, num):
        self.set_num(num)
        self.__bi = self.binario(num)

    def set_num(self, num):
        self.__num = num
    def get_num(self):
        return self.__num

    def binario(self, num):
        bi = bin(num)[2:]
        return bi

    def __str__(self):
        return f"O binario de {self.__num} é {self.__bi}"


b = Conversor(11)
print(b)