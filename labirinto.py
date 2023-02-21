from Ponto import Ponto
from random import randint


class labirinto:

    def __init__(self,largura,altura):
        self.largura = largura # X
        self.altura = altura # Y
        self.matriz = self.inicializa_Matriz_Zero()
        self.ponto_Inicial = None
        self.ponto_Final = None
        self.Gera_Labirinto()
        self.Define_Inicio_Fim()
    
    def acessa_Elemento(self,x,y):
        num = self.matriz[y][x]
        return num
 

    def inicializa_Matriz_Zero(self):
        mat = []     
        for i in range(self.altura):
            lista = [0]*self.largura
            mat.append(lista)
        return mat
    
    def imprime_Matriz(self):
        for i in range(self.altura):
            for j in range(self.largura):
                print(self.matriz[i][j],end=" ")
            print()
    
    def retorna_Corredores(lista_proibida,x,y):
        lista = []
        if (x-1,y,x-2,y) not in lista_proibida :
            lista.append((x-1,y,x-2,y))#esq
            lista_proibida.add((x-1,y,x-2,y))

        if (x,y-1,x,y-2) not in lista_proibida :    
            lista.append((x,y-1,x,y-2))#cima
            lista_proibida.add((x,y-1,x,y-2))

        if (x+1,y,x+2,y) not in lista_proibida :
            lista.append((x+1,y,x+2,y))#dir
            lista_proibida.add((x+1,y,x+2,y))

        if (x,y+1,x,y+2) not in lista_proibida :
            lista.append((x,y+1,x,y+2))#baixo
            lista_proibida.add((x,y+1,x,y+2))

        return lista
        

    def Gera_Labirinto(self):
        lista_proibida = set()
        lista = []

        altura = self.altura
        largura = self.largura

        x=y=0

        while y%2==0 or x%2==0 and(y<altura-2 and x< largura-2):
            y = randint(3,(altura-3))
            x = randint(3,(largura-3))
        
            
        self.matriz[y][x]=1

        lista = labirinto.retorna_Corredores(lista_proibida,x,y)

        while len(lista)> 0 :
            escolha = randint(0,len(lista)-1)
            ponto = lista[escolha]
            lista.pop(escolha)

            if (ponto[2] >= 0) and (ponto[3] >= 0) and (ponto[2]< largura -1) and (ponto[3]<altura-1):
                if (self.matriz[ponto[3]][ponto[2]]==0):
                    self.matriz[ponto[1]][ponto[0]] = 1
                    self.matriz[ponto[3]][ponto[2]] = 1
                    lista += labirinto.retorna_Corredores(lista_proibida,ponto[2],ponto[3])

    def Define_Inicio_Fim(self):
        inicio = randint(1,(self.altura-1))
        while self.matriz[inicio][1] != 1:
             inicio = randint(1,(self.altura-1))
        Ponto_Inicio= Ponto(0, inicio)
        
        fim = randint(1,(self.altura-1))
        while self.matriz[fim][self.largura-2] != 1:
            fim = randint(1,(self.altura-1))
        Ponto_Fim= Ponto(self.largura-1, fim)

        self.matriz[inicio][0] = 1
        self.matriz[fim][self.largura-1] = 1

        self.ponto_Inicial = Ponto_Inicio
        self.ponto_Final = Ponto_Fim



 