#Entidade
class Triangulo:
  def_init_(self):
    self.b = 0
    self.h = 0
  def calc+area(self):
return self.b * self.h/2
 

class UI:
 @staticmethod
 def main():
   x = triangulo()
   x.b = 10
   x.h = 20
   print(x.b, x.h, x.cal_area())
   print(x)

UI.main()
