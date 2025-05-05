class playList:
  def__init__(self, nome, descrição):
    self.__nome = nome
    self.__descrição = descrição
    self.__musicas = []
  def inserir(self, m):
    sef.__musicas.append(m)
  def listar(self):
    return self.__musicas
  def__str__(self):
    return f"PlayList (self.__nome) tem (len(self.__musicas)) musica(s)"

class Musica:
  def__init__(self, titulo, artista, album):
    self.__titulo = titulo
    self.__artista = artista
    self.__album = album
  def__str__(self):
    return f"(self.__titulo) - (self.__artista) - (self.__album)

x = PlayList("Rock", "Minhas músicas de rock preferidas")
y = Playlist("Axê", "show de Ivete Sangalo - Maracanã")
m1 = Musica("Hotel California", "Eagles", "Eagles")
m2 = Musica("Beth Balanço", "Barão Vermelho", "Melhores Musicas")
m3 = Musica("Areré", "Ivete", "Show Macanã")
x.inserir(m1)
x.inserir(m2)
y.inserir(m3)

print(x)
for musica in x.listar()
  print(" ", musica)

print(y)
for musica in y.listar()
  print(" ", musica)
