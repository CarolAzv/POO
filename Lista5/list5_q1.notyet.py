import datetime

class Paciente():
    def __init__(self, nome, cpf, fone, birth):
        self.__nome = nome
        self.__cpf = cpf
        self.__fone = fone
        self.__birth = birth

    def Idade(self):
        date = self.__birth - datetime.datetime.today()
        return f"date"

x = Paciente()
print(x)

    #how do i make "birth" a datetime thing?