from Ponto import Ponto
matriz =([[0,0,0,0,0,0,0,0,0,0], #7x10
        [0,1,0,1,1,1,1,1,1,1], #saida
        [0,1,0,1,0,0,0,0,0,0], # linha 2 coluna 10 fim
        [0,1,0,1,1,1,1,0,0,0], # linha 2 coluna 2 começo
        [0,1,1,0,1,0,1,0,0,0],
        [0,0,1,1,1,0,1,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]])
class Matriz:
    def acessaPonto(x,y):
        return matriz[x][y]

