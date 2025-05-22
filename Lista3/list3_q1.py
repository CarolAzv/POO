class Retangulo():
    def __init__(self, base, alt):
        self.__base = base
        self.__alt = alt
        self.__area = self.calc_area()
        self.__nal = self.calc_nal()

    def set_alt(self, alt):
        self.__alt = alt
    def get_alt(self):
        return self.__alt
    
    def set_base(self, base):
        self.__base = base
    def get_base(self):
        return self.__base
    
    def calc_area(self):
        area = self.__base * self.__alt
        return area

    def calc_nal(self):
        nal = (self.__base * self.__base) + (self.__alt * self.__alt)
        nal = nal ** 0.5
        return round(nal, 2)
    
    def __str__(self):
        return f"O retangulo de base {self.__base} e altura {self.__alt}, tem a área de {self.__area} e a diagonal de {self.__nal}"
    
r = Retangulo(4, 8)
print(r)
