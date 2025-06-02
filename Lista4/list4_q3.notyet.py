class Empresa():
    def __init__(self, nome):
        self.__nome = nome
        self.__clientes = []
    
    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    
    def Inserir(self, c):
        self.__clientes.append(c)
    def Listar(self):
        return self.__clientes
    
    def __str__(self):
        return f"A impresa {self.__nome} tem {len(self.__clientes)} cliente(s)"


class Cliente():
    def __init__(self, nome, cpf, limite, socio):
        self.__nome = nome
        self.__cpf = cpf
        self.__limite = limite
        self.__socio = socio

    def set_nome(self, nome):
         self.__nome = nome
    def get_nome(self):
        return self.__nome
    def set_cpf(self, cpf):
         self.__cpf = cpf
    def get_cpf(self):
        return self.__cpf
    
    def set_socio(self, socio):
         self.__socio = socio
    def get_socio(self):
        return self.__socio
    
    def set_limite(self, limite):
        self.__limite = limite
    def get_limite(self):
        return self.__limite
    
    def __str__(self):
        return f"{self.__nome}, tem limite de R$ {self.__limite}"