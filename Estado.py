from Ponto import Ponto
from Heap import Heap

class Estado:
    def __init__(self,matriz, PontoAtual,PontoFinal, passos, caminho):
        self.PontoAtual = PontoAtual
        self.PontoFinal = PontoFinal
        self.matriz = matriz
        self.caminho = caminho

        #calcula f, g, h
        self.g = passos
        self.h = self.calcula_Heurística()
        self.f = self.g + self.h
    
    def __lt__(self, other):
        return self.f < other.f

    def calcula_Heurística(self):
        return int(Ponto.DistanciaEntreDoisPonto(self.PontoAtual, self.PontoFinal))
    
    
    def transicoes(self, estados_Passados):# 2, 2 
        saida = []

        for i in range(1,5):
            proxEstado, direcao = Ponto.RetornaPonto(self.PontoAtual, i)

            if (self.matriz[proxEstado.y][proxEstado.x] == 1) and ((proxEstado.x, proxEstado.y) not in estados_Passados):
                caminho = self.caminho + [direcao]
                saida.append(Estado(self.matriz, proxEstado, self.PontoFinal, self.g + 1, caminho))
        return saida
    
    
    def __repr__(self):
        return "({})".format(self.PontoAtual)



