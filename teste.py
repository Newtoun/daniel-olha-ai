from Ponto import Ponto

lista = set()
vet = []
a = Ponto(1,1)
lista.add((a.x,a.y))
print(lista)
b = Ponto(2,1)
c = Ponto(3,1)
d = Ponto(1,1)
print((c.x,c.y) in lista)


