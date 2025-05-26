class Frete:
    def __init__(self, dist, peso):
        self.set_dist(dist)
        self.set_peso(peso)
        self.__frete = 0

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
