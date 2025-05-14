class Carrinho:
    def__init__(self, cliente, data, itens):
        self.__nome = nome:str
        self.__data = data
        self.__itens = Item

class Item:
    def__init__(self, produto, qtd, preço_unit):
        self.set_produto(produto)
        self.set_qtd(qtd)
        self.set_preço_unit(preço_unit)
    def set_produto(self, produto):
        if produto = "": raise ValueError("Produto não pode estar fazio")
        self.__produto = produto
    def get_produto(self):
        return self.__produto
    def set_qtd(self, qtd):
        if produto <= 0: raise ValueError("Quantidade precisa ser positivo")
        self.__qtd = qtd
    def get_qtd(self):
        return self.__qtd
    def set_preço_unit(self, preço_unit):
        if produto <= 0: raise ValueError("Preço da unidade precisa ser positivo")
        self.__preço_unit = preço_unit
    def get_preço_unit(self):
        return self.__preço_unit
    def Total(self, produto, qtd, preço_unit):
        total = 0
        for produto in self.__produto:
            total += (Item.get_preço_unit * Item.get_qtd)
