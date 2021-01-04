import pygame
import time
import cores
import objetos_e_personagens as obp
import Textos

pygame.init()

#VARIAVEIS
font = pygame.font.SysFont(Textos.fonte1.Estilo, Textos.fonte1.Tamanho)

#Pegar personagem
X = obp.p1.X
Y = obp.p1.Y
HEIGHT = obp.p1.heigth
WIDTH = obp.p1.width

#GERAR TELA
def windown():
    screen = pygame.display.set_mode((800, 800),0,32)
    pygame.display.set_caption('Teste1')

    screen.fill([150, 200, 180])
    #pygame.draw.line(screen, cores.Cores['CIAN'], [10, 100], [630, 100], 5)
    pygame.draw.rect(screen, cores.Cores['RED'], [X, Y, HEIGHT, WIDTH])

    text = font.render(Textos.Textos['Teste'], True, cores.Cores['BLACK'])

    #screen.blit(text, [350, 200])
    
    pygame.display.update()
  
run = True
while run == True:
    pygame.time.delay(100)

    event = pygame.event.poll()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Key = pygame.key.get_pressed()

    if Key[pygame.K_LEFT]:
        X -= obp.p1.velX
        if X < 0:
            X = 800
    
    if Key[pygame.K_RIGHT]:
        X += obp.p1.velX
        if X > 800:
            X = 0
        

    if Key[pygame.K_UP]:
        Y -= obp.p1.velY
        if Y < 0:
            Y = 800

    if Key[pygame.K_DOWN]:
        Y += obp.p1.velY
        if Y > 800:
            Y = 0
        
    windown()
    
pygame.exit()
