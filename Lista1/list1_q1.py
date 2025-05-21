class Viagem:
    def __init__(self, dist, tempo):
        self.__dist = dist
        self.__tempo = tempo
        self.__vel = 0

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


    def veloc(self, dist, tempo):
        vel = (get_dist)/(get_tempo)
        set_vel(self, vel)
        return get_vel

    def __str__(self):
        f = "Viagaram por "
        f += str(self.__dist)
        f += "Km, por "
        f += str(self.__tempo)
        f += " hora(s) a "
        f += str(self.get_vel())
        f += "Km/h"
        return f
        #return f"Viagaram por {}Km, por {} hora(s) a {}Km/h".format(self.__dist, self.__tempo, self.__vel))


x = Viagem(100, 2.5)
print(x)
