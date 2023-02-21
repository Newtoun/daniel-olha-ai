from labirinto import labirinto
from Estado import Estado
from Gabarito import Gabarito
import pygame

pygame.init()

screen = pygame.display.set_mode((1800,900))
pygame.display.set_caption("Labirinto")

speed = 25
matriz = labirinto(57,27)

estadoInicial = Estado(matriz.matriz,matriz.ponto_Inicial,matriz.ponto_Final,0, [])
resposta = Gabarito.busca_Informada(estadoInicial)

x = matriz.ponto_Inicial.x*25
y = matriz.ponto_Inicial.y*25
map = matriz.matriz

def executa_Caminho_Gabarito(caminho):
    for i in range(len(caminho)):
        if caminho[i]=='left':
            x -= speed
        if caminho[i]=='right':
            x += speed
        if caminho[i]=='up':
            y -= speed
        if caminho[i]=='down':
            y += speed

def game_map():

    global rect_one
    surface = pygame.Surface((100, 100), pygame.SRCALPHA)
    rect_one = pygame.draw.rect(surface, (0, 80, 75), (0, 0, 25, 25)) 

    global rect_two
    surface_one = pygame.Surface((80, 80), pygame.SRCALPHA)
    rect_two = pygame.draw.rect(surface_one, (0, 255, 255), (0, 0, 25, 25)) 

    tileX = 0
    tileY = 0
    
    for y, row in enumerate(map):
        tileX = 0
        for x, cell in enumerate(row):
            image = surface_one if cell == 0 else surface
            screen.blit(image, [x*25, y*25]) 
    pygame.display.update() 


def player():
    player = pygame.draw.rect(screen, (255,0,0), (x, y, 25, 25))   

loop = True
i = 0
while loop:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False

    #player controls
    keys = pygame.key.get_pressed()
    
    pos = x, y
    #if keys[pygame.K_LEFT]:
    #    x -= speed
    #if keys[pygame.K_RIGHT]:
    #    x += speed
    #if keys[pygame.K_UP]:
    #    y -= speed
    #if keys[pygame.K_DOWN]:
    #    y += speed
    
    if resposta[i]=='left':
        x -= speed
    if resposta[i]=='right':
        x += speed
    if resposta[i]=='up':
        y -= speed
    if resposta[i]=='down':
        y += speed
    pygame.time.delay(300)
    i+=1
    row = y // 25
    column = x // 25
    if map[row][column] == 0:
        x, y = pos

    screen.fill((255,255,255))
    game_map()
    player()
    pygame.display.update()


pygame.quit()