class Bancaria:
    def __init__(self, nome, numero, saldo, met):
        self.__nome = nome
        self.__numero = numero
        self.__saldo = saldo
        self.__met = self.set_met()

    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    
    def set_numero(self, numero):
        self.__numero = numero
    def get_numero(self):
        return self.__numero
    
    def set_saldo(self, saldo):
        self.__saldo = saldo
    def get_saldo(self):
        return self.__saldo
    
    def set_met(self, met):
        if met == 3:
            self.__saldo = ["cartão, boleto e pix"]
        elif met == 2:
            self.__saldo = map(str, input("Selecione 2 entre os seguintes métodos: cartão, boleto ou pix").split())
        elif met == 1:
            self.__saldo = map(str, input("Selecione 1 entre os seguintes métodos: cartão, boleto ou pix").split())
    def get_met(self):
        return self.__met
    

    def __str__(self):
        return f"{self.__nome}, {self.__numero}, tem {self.__saldo} e os seguintes métodos de trancição permetidos: ----"
    
x = "aaaaaaaaaaaaaaaaa"
