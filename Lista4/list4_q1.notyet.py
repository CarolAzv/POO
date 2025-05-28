import random
      # how do i make it do thing??????
class Bingo:
    def __init__(self, numb):
        self.__numb = numb
        self.__bolas = []

    def Proximo():
        x = random.randrange(0, self.__numb)
        if x not in self.__bolas:
            self.__bolas.append(num)
            print(x)
        else:
            return Proximo()

    def Sorteados(num):
        self.__bolas.append(num)
        return self.__bolas


x = Bingo(5)
print(x)