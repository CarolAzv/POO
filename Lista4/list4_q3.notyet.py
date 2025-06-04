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

class UI:
    def menu():
        return int(input("Menu: 1-Criar Empresa, 2-Listar clientes, 3-definir sociedade, 9-sair"))
    
    def main():
        opt = 0
        x = None
        while opt != 9:
            opt = UI.menu()
            if opt == 1:
                x = UI.criar_empresa()
            if opt == 2:
                x = UI.listar_clientes
            if opt == 3:
            if opt == 9:



    @staticmethod
    def criar_empresa():
        nome = input("Informe o nome da impresa: ")
        x = Empresa(nome)

    @staticmethod
    def listar_clientes(x):
        input(x)
        for clientes in x.Listar():
            print(" ", clientes)

    @staticmethod
    def defenir_sociedade():
        input(x)
        n = 0
        clientes = x.listar()
        for cliente in x.listar():
            print(x, "-", cliente)
            n += 1
        a = int(input("Informe o n do 1 cliente: ")
        b = int(input("Informe o n do 2 cliente: ")
        clientes[a].set_social(cliente[b])
Ui.main()

x = Empresa("parasocio")
a = Cliente("Bianca", 155.732156012, 2500, "")
b = Cliente("Andre", 105.235789343, 5000, "")
x.Inserir(a)
x.Inserir(b)

print(x.Listar())
