class Frete:
    def __init__(self, peso, dist):
        self.set_peso(peso)
        self.set_dist(dist)
        self.__frete = self.calc_frete()

    def set_dist(self, dist):
        if dist < 0: raise ValueError("Distância não pode ser negativo")
        self.__dist = dist
    def get_dist(Self):
        return self.__dist

    def set_peso(self, peso):
        if peso < 0: raise ValueError("Peso não pode ser negativo")
        self.__peso = peso
    def get_peso(Self):
        return self.__peso

    def calc_frete(self):
        frete = self.__dist * self.__peso
        frete = frete * 0.01
        return frete
    
    def __str__(self):
            return f"O frete de transportar {self.__peso}Kg por {self.__dist}Km sera: R${self.__frete}"


x = Frete(60, 150)
print(x)
