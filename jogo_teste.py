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
screen = pygame.display.set_mode((800, 800),0,32)
framerate = float(8)
colisaoo = False
#GERAR TELA
def windown():
    pygame.display.set_caption('Teste1')
    
    screen.fill(cores.Cores['WHITE'])
    pygame.draw.rect(screen, cores.Cores['BLACK'], [obp.p1.X, obp.p1.Y, obp.p1.heigth, obp.p1.width])
    pygame.draw.rect(screen, cores.Cores['RED'], [obp.maca.X, obp.maca.Y, obp.maca.height, obp.maca.width])
    if obp.p1.eat != 0:
        text = font.render(str(obp.p1.eat), True, cores.Cores['MUSGO'])

        screen.blit(text, [750, 0])

    pygame.display.update() 
    relogio.tick(framerate)
    print(framerate)

run = True   
while run == True:
    event = pygame.event.poll()

    #evento para sair do game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #tecla chave sendo pressionada
    Key = pygame.key.get_pressed()
    #colisão de objeto
    colisaoo = funcoes.colision(framerate, colisaoo)
    #reframe da tela
    if colisaoo == True:
        framerate = funcoes.velocidadeframe(framerate)
        
    windown()
    #teste de parada do game
    run = funcoes.perdeu()
    #movimentação
    funcoes.funcao_movimento(Key, font, screen)
    #movimento constante
    obp.p1.X += obp.p1.velX
    obp.p1.Y += obp.p1.velY
    colisaoo = False

con = font.render('Seu placar foi de: ', True, cores.Cores['PINK'])
fim = font.render(str(obp.p1.eat), True, cores.Cores['PINK'])
screen.blit(con, [250, 350])
screen.blit(fim, [400, 400])
pygame.display.update()





