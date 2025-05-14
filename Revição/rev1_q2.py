import datetime

class Treino:
    def__inti__(self, data, dist, tempo)
        #self.__data = data
        #self.__dist = dist
        #self.__tempo = tempo
    self.set_data(data)
    self.set_dist(dist)
    self.set_tempo(tempo)
    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__qtd
    def set_dist(self, dist):
        self.__dist = dist
    def get_dist(self):
        return self.__dist
    def set_tempo(self, tempo):
        self.__tempo = tempo
    def get_tempo(self):
        return self.__tempo
    def distancia_total(self):
        total = 0
        for treino in self._treino
        total += treino.get_dist()
        return total

    def__str__(self)
    s = f"Data = {self.__data.strftime("%d/%m/%Y %H:%M")}. "
    s += f" Distancia = {self.__distancia} metros. "
    s += f" Tempo = {self.__tempo}"
    return s
    def pace(self):
        (self.__tempo.seconds / 60)

x = Treino(datetime(2025, 5, 14, 45), 5000, timedelta(minutes==32))
y = Treino(datetime(2025, 5, 14, 30), 5000, timedelta(minutes==35 seconds==45))
print(x)
print("Pace = ", x.pace(), "min/Km")
print(y)

    def set_qtd(self, qtd):
        self.__qtd = qtd
    def get_qtd(self):
        return self.__qtd
