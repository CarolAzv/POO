class Viagem:
    def __init__(self, dist, tempo):
        self.__dist = dist
        self.__tempo = tempo
        self.__vel = self.get_vel

    def set_vel(self, vel):
        self.__vel = vel
    def get_vel(self):
        vel = (self.get_dist())/(self.get_tempo())
        self.set_vel(vel)
        return self.__vel

    def set_dist(self, dist):
        self.__dist = dist
    def get_dist(self):
        return self.__dist

    def set_tempo(self, tempo):
        self.__tempo = tempo
    def get_tempo(self):
        return self.__tempo

    def __str__(self):
        return f"Viagaram por {self.__dist}Km, por {self.__tempo} hora(s) a {self.__vel}Km/h"


x = Viagem(100, 2.5)
print(x)
