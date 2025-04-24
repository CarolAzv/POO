class Contabancaria:
    def _init_(self):
        self.titular = "titular"
        self.numero = "0000-0"
        self.saldo = 0
    def set_titular(self, v):
        if v == "": raise ValueError("Titular não pode ser vazio")
        self.titular = v
    def get_titular(self):
        return self._titular
    def set_numero(self, v):
        if v == "": raise ValueError("Numero da conta não pode ser vazio")
        self.titular = v
    def get_numero(self):
        return self._numero
    def set_saldo(self, v):
        if v == "": raise ValueError("Numero da conta não pode ser vazio")
        self.titular = v
    def get_saldo(self):
        return self._numero
    def depositar(self, v):
        if v <= 0: raise ValueError("Valor não pode ser negativo")
        self.titular += v
    def sacar(self, v):
        if v <= 0: raise ValueError("Valor não pode ser negativo")
        if v>self._saldo: raise ValueError("")