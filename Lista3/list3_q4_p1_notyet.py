class Equação2g():
    def __init__(Self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__delta = self.Delta()

    def set_a(self, a):
        self.__a = a
    def set_a(self, b):
        self.__b = b
    def set_a(self, c):
        self.__c = c

    def get_a(self, a):
        self.__a = a
    def get_a(self, b):
        self.__b = b
    def get_a(self, c):
        self.__c = c

    def Delta(self):
        delta = (self.__b * self.__b) - (4 * self.__a * self.__c)
        return delta
    def Raiz1(self):
        raiz = -b + (self.__delta * 0.5)
        raiz = raiz / (2 * self.__a)
        return raiz
    def Raiz2(self):
        raiz = -b - (self.__delta * 0.5)
        raiz = raiz / (2 * self.__a)
        return raiz
    def TemRaizesReais(self):
        