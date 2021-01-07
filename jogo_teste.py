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
relogio = pygame.time.Clock()

#GERAR TELA
def windown():
    screen = pygame.display.set_mode((800, 800),0,32)
    pygame.display.set_caption('Teste1')
    
    screen.fill(cores.Cores['WHITE'])
    pygame.draw.rect(screen, cores.Cores['BLACK'], [obp.p1.X, obp.p1.Y, obp.p1.heigth, obp.p1.width])
    if obp.p1.eat != 0:
        pygame.draw.rect(screen, cores.Cores['BLACK'], [funcoes.mostrarCorpo(), funcoes.mostrarCorpo(), obp.corpo.height, obp.corpo.width])

    pygame.draw.rect(screen, cores.Cores['RED'], [obp.maca.X, obp.maca.Y, obp.maca.height, obp.maca.width])
    if obp.p1.eat != 0:
        text = font.render(str(obp.p1.eat), True, cores.Cores['MUSGO'])

        screen.blit(text, [750, 0])

    pygame.display.update()
    relogio.tick(10)


run = True   
while run == True:
    event = pygame.event.poll()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    Key = pygame.key.get_pressed()
    funcoes.colision()
    funcoes.funcao_movimento(Key)
    windown()
    obp.p1.X += obp.p1.velX
    obp.p1.Y += obp.p1.velY
    obp.corpo.X += obp.p1.velX
    obp.corpo.Y += obp.p1.velY
    
pygame.quit()
