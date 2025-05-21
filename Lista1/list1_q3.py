class Bancaria:
    def __init__(self, nome, numero, saldo, met):
        self.__nome = nome
        self.__numero = numero
        self.__saldo = saldo
        self.__met = met

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
        self.__met = met
    def get_met(self):
        return self.__met
    

    def __str__(self):
        return f"{self.__nome} {self.__numero}, tem R${self.__saldo} de saldo e os seguintes métodos de trancição permetidos: {self.__met}"
    
x = Bancaria("Lucas", 199189, 2500, "cartão de credito, boleto e pix")
print(x)
