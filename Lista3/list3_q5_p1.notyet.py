class Data:
    def __init__(self, dia, mes, ano):
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def get_dia(self, dia):
        return self.__dia
    def get_mes(self, mes):
        return self.__mes
    def get_ano(self, ano):
        return self.__ano

    def __str__(self):
        return f"{self.__dia}/{self.__mes}/{self.__ano}"


a = Data(5,10,2005)
print(a)