class PlayList():
    def __init__(self, nome, descrição):
        self.__nome = nome
        self.__descrição = descrição
        self.__musicas = []
    
    def set_nome(self, nome):
        self.__nome = nome
    def set_descrição(self, descrição):
        self.__descrição = descrição
    def get_nome(self):
        return self.__nome
    def get_descrição(self):
        return self.__descrição
    
    def Inserir(self, musica):
        self.__musicas.append(musica)
    def Listar(self):
        return self.__musicas
    
    def __str__(self):
        return f"PlayList {self.__nome} tem {len(self.__musicas)} musica(s)"

class Musica():
    def __init__(self, titulo, artista, album):
        self.__titulo = titulo
        self.__artista = artista
        self.__album = album

    def set_titulo(self, titulo):
        self.__titulo = titulo
    def set_artista(self, artista):
        self.__artista = artista
    def set_album(self, album):
        self.__album = album
    def get_titulo(self):
        return self.__titulo
    def get_artista(self):
        return self.__artista
    def get_album(self):
        return self.__album
    
    def __str__(self):
        return f"{self.__titulo} - {self.__artista}, {self.__album}"
    
x = PlayList("Rock", "Minhas músicas de rock preferidas")
y = PlayList("Axê", "show de Ivete Sangalo - Maracanã")
m1 = Musica("Hotel California", "Eagles", "Eagles")
m2 = Musica("Beth Balanço", "Barão Vermelho", "Melhores Musicas")
m3 = Musica("Areré", "Ivete", "Show Macanã")
x.inserir(m1)
x.inserir(m2)
y.inserir(m3)

print(x)
for musica in x.listar():
  print(" ", musica)

print(y)
for musica in y.listar():
  print(" ", musica)