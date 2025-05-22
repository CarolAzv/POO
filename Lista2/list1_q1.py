class Circulo:
    def __init__(self, raio):
        self.__raio = raio
        self.__area = self.set_area()
        self.__rencia = self.set_rencia()

    def set_raio(self, raio):
        self.__raio = raio
    def get_raio(self):
        return self.__raio
    
    def set_area(self):
        r = self.__raio
        area = r * r
        area = area * 3.14
        self.__area = round(area, 2)
        return self.__area
    def get_area(self):
        return self.__area
    
    def set_rencia(self):
        rencia = 3.14 * 2 * self.__raio
        self.__rencia = round(rencia, 2)
        return self.__rencia
    def get_rencia(self):
        return self.__rencia
    
    def __str__(self):
        return f"O circulo de raio {self.__raio} tera uma área de {self.__area} e uma circunferência de {self.__rencia}"
    
x = Circulo(5)
print(x)