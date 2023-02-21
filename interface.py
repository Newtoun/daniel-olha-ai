from pygame.locals import *
import pygame
from Estado import Estado
from Ponto import Ponto
from Gabarito import Gabarito
from labirinto import labirinto
import time

velocidade  = 0.05
class Jogador:
    #posição inicial do jogador
    def __ini__(self):
        self.x = None
        self.y = None
        self.speed = 0.3 # passos por  vez (velocidade)
 
    def moverDireita(self):
        self.x +=velocidade
 
    def moverEsquerda(self):
        self.x -= velocidade
 
    def moverCima(self):
        self.y -=velocidade
 
    def moverBaixo(self):
        self.y +=velocidade
 
class tela: #mudar para labirinto e mudar aquele que tem o nome de labirinto
    def __init__(self, matriz):
       self.M = matriz.largura
       self.N = matriz.altura
       self.maze = matriz.matriz

    def draw(self,display_surf,image_surf): #vai desenhar o labirinto

       for i in range(self.N):
        for j in range (self.M):
            if self.maze[i][j] == 0:
               display_surf.blit(image_surf,( j * 44 , i * 44)) #desenhar a imageSurf na janela (labirinto)

class App:
 
    def __init__(self, matriz):
        self.windowWidth = matriz.largura *44 #tamanhos
        self.windowHeight = matriz.altura *44
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        self.player = Jogador() #jogador onde tenho que passar o inicio de onde ele vai fica
        self.player.x = matriz.ponto_Inicial.x*44
        self.player.y = matriz.ponto_Inicial.y*44

        self.maze = tela(matriz) #tenho que passar a matriz

    def isnotCollision(self,direcao):
       x = self.player.x / 44
       y = self.player.y / 44
       if direcao == 'rigt':
            if self.maze.maze[int(y)][int(x + velocidade)] != 0:
                return True
       elif direcao == 'left':
            if self.maze.maze[int(y )][int(x - velocidade)] != 0:
                return True
       elif direcao == 'up':
            if self.maze.maze[int(y - velocidade)][int(x)] != 0:
                return True
       elif direcao == 'down':
            if self.maze.maze[int(y + velocidade)][int(x)] != 0:
                return True
       return False

    def on_init(self): #inicializa a parte do pygame
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE) #inicializa uma janela
        
        pygame.display.set_caption('Labirinto') #define a legenda da janela
        self._running = True
        self._image_surf = pygame.image.load("bola.png").convert() #carrega imagem do jogador
        self._block_surf = pygame.image.load("dA.png").convert() #carrega os bloqueios
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        pass #deixa passar de bobs
    
    def on_render(self):
        self._display_surf.fill((0,0,0)) #preencher a superfície com uma cor sólida
        self._display_surf.blit(self._image_surf,(self.player.x,self.player.y)) #desenhar uma imagem sobre outra
        self.maze.draw(self._display_surf, self._block_surf) #vai desenhar as paredes e o jogador
        pygame.display.flip() #virar verticalmente e horizontalmente
 
    def on_cleanup(self):
        pygame.quit() #termina o pygame
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() #obter o estado de todos os botões do teclado
            
            #movimentação do jogador
            if (keys[K_RIGHT]):
                if self.isnotCollision('rigt'):
                    self.player.moverDireita()
                else:
                     pygame.event.pump()
                     keys = pygame.key.get_pressed()
 
            if (keys[K_LEFT]):
                if self.isnotCollision('left'):
                    self.player.moverEsquerda()
                else:
                     pygame.event.pump()
                     keys = pygame.key.get_pressed()
 
            if (keys[K_UP]):
                if self.isnotCollision('up'):
                    self.player.moverCima()
                else:
                    pygame.event.pump()
                    keys = pygame.key.get_pressed()
 
            if (keys[K_DOWN]):
                if self.isnotCollision('down'):
                    self.player. moverBaixo()
                else:
                    pygame.event.pump()
                    keys = pygame.key.get_pressed()

                
            if (keys[K_ESCAPE]):
                self._running = False
 
            self.on_loop()
            self.on_render() #acho que atualiza a tela
        self.on_cleanup() #finalizar

    def executa_Caminho_Gabarito(self, caminho):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed()
            for i in caminho:
                if i == 'up':
                    self.player.moverCima()
                elif i == 'down':
                    self.player.moverCima()
                elif i == 'left':
                    self.player.moverEsquerda()
                elif i == 'right':
                    self.player.moverDireita()
                self.on_loop()
                self.on_render()
            if (keys[K_ESCAPE]):
                self._running = False
        self.on_cleanup()
if __name__ == "__main__" :
    matriz = labirinto(23,13)
    inicio = matriz.ponto_Inicial
    fim = matriz.ponto_Final
    print("ini: {} fim: {}".format(inicio,fim))
    matriz.imprime_Matriz()
    
    estadoInicial = Estado(matriz.matriz,inicio,fim,0, [])
    resposta = Gabarito.busca_Informada(estadoInicial) 
    
    if resposta == 0:
        print("Labirinto não tem solução")
    else: 
        print(resposta)
    theApp = App(matriz)
    theApp.on_execute()
    #theApp.executa_Caminho_Gabarito(resposta)
