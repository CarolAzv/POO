class Carrinho:
    def__init__(self, cliente, data, itens):
        self.__nome = nome:str
        self.__data = data
        self.__itens = Item

class Item:
    def__init__(self, produto, qtd, preço_unit):
        self.__produto = produto#:str
        self.__qtd = qtd#:int
        self.__preço_unit = preço_unit#:double
    def set_produto(self, produto):
        self.__produto = produto
    def get_produto(self):
        return self.__produto
    def set_qtd(self, qtd):
        self.__qtd = qtd
    def get_qtd(self):
        return self.__qtd
    def set_preço_unit(self, preço_unit):
        self.__preço_unit = preço_unit
    def get_preço_unit(self):
        return self.__preço_unit
    def Total(self, qtd, preço_unit):
