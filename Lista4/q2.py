class playList:
  def __init__(self, nome, descrição):
    self.__nome = nome
    self.__descrição = descrição
    self.__musicas = []
  def inserir(self, m):
    self.__musicas.append(m)
  def listar(self):
    return self.__musicas
  def __str__(self):
    return f"PlayList (self.__nome) tem (len(self.__musicas)) musica(s)"

class Musica:
  def __init__(self, titulo, artista, album):
    self.__titulo = titulo
    self.__artista = artista
    self.__album = album
  def __str__(self):
    return f"{self.__titulo} - (self.__artista) - (self.__album)"
    
class UI:
  @statecmethod
  def menu():
    print("Menu: 1-Criar PlayList, 2-Inserir Musica. 3- listar Musica, 9-Fim")

  @statecmethod
  def mein():
    op = 0
    x = None
    while op != 9:
      if op == 1: x = UI.criar_playlist()
      if op == 2:
        if x == None: print("Crie uma playlist antes!")
        else: UI.inserir_musica(x)
      if op == 3:
        if x == None: print("Crie uma playlist antes!")
        else: UI.listar_musica(x) 

  @statecmethod
  def criar_playlist():
    nome = input("informe o nome da playlist")
    descrição = input("informe uma descrição")
    x = PlayList(nome, descrição)
    return x
    
  @statecmethod
  def inserir_musica(x):
    titulo = input("informe o titulo da musica: ")
    artista = input("informe o artista/banda: ")
    album - input("informe o álbum: ")
    musica = Musica(titulo, artista, album)
    x.inserir(musica)

  @statecmethod
  def listar_musica(x):
    print(x)
    for musica in x.listar()
      print(" ", musica)


UI.main()
    

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
