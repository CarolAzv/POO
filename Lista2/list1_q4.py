class Cinema:
    def __init__(self, dia, hora):
        self.__dia = dia
        self.__hora = hora
        self.__inteira = self.set_inteira(dia)
        self.__meia = self.set_meia()

    def set_dia(self, dia):
        self.__dia = dia
    def get_dia(self):
        return self.__dia
    
    def set_hora(self, hora):
        self.__hora = hora
    def get_hora(self):
        return self.__hora
    
    def set_inteira(self, dia):
        barato = ["segunda", "terça", "quarta", "quinta"]
        mais = [17, 18, 19, 20, 21, 22, 23, 24, 0]
        if self.__dia in barato:
            self.__inteira = "R$ 16,00"
            if self.__hora in mais:
                self.__inteira = "R$ 24,00"
        else:
            self.__inteira = "R$ 20,00"
            if self.__hora in mais:
                self.__inteira = "R$ 30,00"
        return self.__inteira
    def get_inteira(self):
        return self.__inteira

    def set_meia(self):
        barato = ["segunda", "terça", "quarta", "quinta"]
        mama = [17, 18, 19, 20, 21, 22, 23, 24, 0]
        dia = self.get_dia()
        self.__meia = "R$ 8,00"
        if (self.get_hora()) in mama and dia in barato and dia != "quarta":
            self.__meia = "R$ 12,00"
        elif (self.get_hora()) in mama and dia not in barato:
           self.__meia = "R$ 15,00"
        return self.__meia
    def get_meia(self):
        return self.__meia
    
    def __str__(self):
        return f"na {self.__dia} as {self.__hora}h o preso da entrada inteira estara {self.__inteira} e a meia-entrada estara {self.get_meia()}"
    
y = Cinema("quarta", 15)
print(y)
