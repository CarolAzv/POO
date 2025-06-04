class Cliente:
    def __init__(self, id, nome, email, fone):
        self.__id = id
        self.__nome = nome
        self.__email = email
        self.__fone = fone

    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_email(self, email):
        self.__email = email
    def set_fone(self, fone):
        self.__fone = fone

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_email(self):
        return self.__email
    def get_fone(self):
        return self.__fone
    
    def __str__(self):
        return f"ID: {self.__id}, Nome: {self.__nome}, email: {self.__email}, Numero: {self.__fone}"

class Clientes:
    def __init__(self):
        self.__clientes = []

    def set_cliente(self, c):
        self.__clientes.append(c)
    def Listar(self):
        return self.__clientes
    #def Listar_id(self):
        #return self.__clientes.Cliente.self__id
    def Atualizar(self, old, new):
        index = self.__clientes.index(old)
        self.__clientes[index] = new
    def Excluir(self, c):
        index = self.__clientes.index(c)
        self.__clientes.pop(index)
    #def Abrir(self):
    #def Salvar(self):

class UI:
    @staticmethod
    def menu():
        return int(input("Menu: 1-Listar Clientes. 2-Enserir Clientes, 3-Atualizar Cliente, 4-Excluir Cliente, 9-Fim"))

    @staticmethod
    def main():
        op = 0
        x = None
        while op != 9:
            op = UI.menu()
            if op == 1:
                x = UI.Listar_Clientes()
            if op == 2:
                x =Clientes.set_cliente()
            if op == 3:
                x =Clientes.Atualizar()
            if op == 4:
                x = Clientes.Excluir()

    @staticmethod
    def Listar_Clientes(x):
        print(x)
        for Cliente in x.Listar():
            print(" ", Clientes)


UI.main()

self, id, nome, email, fone
x = Cliente(123, "Shelly", "@sure", 199)
y = Cliente(254, "Arthur", "@HEY!", 181)

a = Clientes()
a.append(x)
a.append(y)
