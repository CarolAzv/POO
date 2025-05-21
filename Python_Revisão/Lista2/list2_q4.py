base = int(input("Digite a base e a altura do retângulo: "))
altura = int(input())

area = base * altura
peri = (base*2) + (altura*2)
dia = (peri + area) ** 0.5

print("Área = {} - Perímetro = {} - Diagonal = {}".format(area, peri, int(dia)))