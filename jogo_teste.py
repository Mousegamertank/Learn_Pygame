import pygame
import time
import cores
import objetos_e_personagens as obp
import Textos
import funcoes

pygame.init()

#VARIAVEIS
font = pygame.font.SysFont(Textos.fonte1.Estilo, Textos.fonte1.Tamanho)
vel_X = 20
vel_Y = 20

#GERAR TELA
def windown():
    screen = pygame.display.set_mode((800, 800),0,32)
    pygame.display.set_caption('Teste1')

    screen.fill(cores.Cores['WHITE'])
    #pygame.draw.line(screen, cores.Cores['CIAN'], [10, 100], [630, 100], 5)
    pygame.draw.rect(screen, cores.Cores['BLACK'], [obp.p1.X, obp.p1.Y, obp.p1.heigth, obp.p1.width])
    pygame.draw.rect(screen, cores.Cores['RED'], [obp.maca.X, obp.maca.Y, obp.maca.heigth, obp.maca.width])
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
    funcoes.funcao_movimento(Key)
    windown()
    obp.p1.X += obp.p1.velX
    obp.p1.Y += obp.p1.velY
    
pygame.quit()
