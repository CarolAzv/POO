class Equação2g():
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__delta = self.Delta()
        self.__raiz1 = self.Raiz1()
        self.__raiz2 = self.Raiz2()
        self.__raizreal = []
        self.TemRaizesReais()

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
        raiz = -self.__b + (self.__delta * 0.5)
        raiz = raiz / (2 * self.__a)
        return raiz
    def Raiz2(self):
        raiz = -self.__b - (self.__delta * 0.5)
        raiz = raiz / (2 * self.__a)
        return raiz
    def TemRaizesReais(self):
        if self.__raiz1 >= 0:
            self.__raizreal.append(self.__raiz1)
        if self.__raiz2 >= 0:
            self.__raizreal.append(self.__raiz2)
        return self.__raizreal

    def __str__(self):
        return f"{self.__raizreal}"


x = Equação2g(3, 2, 3)
print(x)
