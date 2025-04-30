Class Retangulo:
    def retangulo
        self.__b = 0
        self.__h = 0

class UI:
    @staticmethod
    def main():
        x = Triangulo(10, 20)
        print(x.calc_area())
        x.set_base(30)
        x.set_altura(40)
        print(x.calc_area())
