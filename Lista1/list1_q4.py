class Cinema:
    def __init__(self, dia, hora):
        self.__dia = dia
        self.__hora = hora
        self.__inteira = 0
        self.__meia = 0

    def set_dia(self, dia):
        self.__dia = dia
    def get_dia(self):
        return self.__dia
    
    def set_hora(self, hora):
        self.__hora = hora
    def get_hora(self):
        return self.__hora
    
    def set_inteira(self):
        barato = ["segunda", "terça", "quarta", "quinta"]
        mais = [17, 18, 19, 20, 21, 22, 23, 24, 0]
        if (self.get_dia()) in barato:
            self.__inteira = "R$ 16,00"
            if (self.get_hora()) in mais:
                self.__inteira = "R$ 24,00"
        else:
            self.__inteira = "R$ 20,00"
            if (self.get_hora()) in mais:
                self.__inteira = "R$ 30,00"
    def get_inteira(self):
        return self.__inteira

    def set_meia(self):
        barato = ["segunda", "terça", "quarta", "quinta"]
        mais = [17, 18, 19, 20, 21, 22, 23, 24, 0]
        dia = self.get_dia()

        self.__meia = "R$ 8,00"
        if (self.get_hora()) in mais and dia in barato and dia != "quarta":
            self.__meia = "R$ 12,00"
        if (self.get_hora()) in mais and dia not in barato:
           self.__meia = "R$ 15,00" 
    def get_meia(self):
        return self.__meia
