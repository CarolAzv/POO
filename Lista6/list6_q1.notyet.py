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

    def get_id(self, id):
        return self.__id
    def get_nome(self, nome):
        return self.__nome
    def get_email(self, email):
        return self.__email
    def get_fone(self, fone):
        return self.__fone
    
    def __str__(self):
        return f"ID: {self.__id}, Nome: {self.__nome}, email: {self.__email}, Numero: {self.__fone}"

class Clientes:
    def __init__(self):
        self.__

    def set_cliente(self):

    def Listar(self):

    def Listar_id(self):

    def Atualizar(self):

    def Excluir(self):

    def Abrir(self):

    def Salvar(self):

class UI:
    @statecmethod
    def menu():
        print("Menu: 1-Criar Cliente, 2-Listar Clientes. 3-Enserir Clientes, 4-Atualizar Cliente, 5-Excluir Cliente, 9-Fim")

    @statecmethod
    def mein():
        op = 0
        x = None
        while op != 9:
            if op == 1: x = UI.criar_cliente()
            if op == 2:
                UI.inserir_musica(x)
            if op == 3:
                UI.listar_musica(x)
            if op == 4:
                UI.listar_musica(x)
            if op == 5:
                UI.listar_musica(x)
    
    @statecmethod
    def criar_cliente():
