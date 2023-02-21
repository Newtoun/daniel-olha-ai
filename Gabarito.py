from Estado import Estado
from Heap import Heap
from Ponto import Ponto


class Gabarito:

    def retorna_Movimento(lista):
     string = []
     for i in range(len(lista)-1):
          if lista[i][0]==lista[i+1][0] and lista[i][1]<lista[i+1][1]:
               string.append("down")
          elif lista[i][0]==lista[i+1][0] and lista[i][1]>lista[i+1][1]:
               string.append("up")
          elif lista[i][1]==lista[i+1][1] and lista[i][0]<lista[i+1][0]:
               string.append("right")
          else:
               string.append("left")
     return string
    
    
    def busca_Informada(estado):
        fila_De_Prioridade = [] # heapMinima
        estados_Passados = set()
        estado_Atual = estado
        #estado_Atual.caminho = [(estado_Atual.PontoAtual.x, estado_Atual.PontoAtual.y)]
        fila_De_Prioridade.append(estado_Atual)
        vetor = []
        while len(fila_De_Prioridade) > 0:
            if (estado_Atual.PontoAtual.x == estado_Atual.PontoFinal.x) and  (estado_Atual.PontoAtual.y == estado_Atual.PontoFinal.y):
                #estados_Passados.add((estado_Atual.PontoAtual.x, estado_Atual.PontoAtual.y))
                #vet = estado_Atual.caminho
                #comandos = Gabarito.retorna_Movimento(vet)
                return estado_Atual.caminho

            estados_Passados.add((estado_Atual.PontoAtual.x, estado_Atual.PontoAtual.y))

            vetor = Estado.transicoes(estado_Atual, estados_Passados)

            fila_De_Prioridade = Heap.atualizar_Heap(fila_De_Prioridade, vetor)

            fila_De_Prioridade = Heap.remover_Primeiro_Elemento(fila_De_Prioridade)

            if len(fila_De_Prioridade)!=0:# tratar o caso que nao tem solucao
                estado_Atual = fila_De_Prioridade[0]
        
        return 0
    
