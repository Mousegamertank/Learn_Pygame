import pygame
import time
import cores
import objetos_e_personagens as obp
import Textos

pygame.init()

#VARIAVEIS
font = pygame.font.SysFont(Textos.fonte1.Estilo, Textos.fonte1.Tamanho)

#GERAR TELA
def windown():
    screen = pygame.display.set_mode((800, 800),0,32)
    pygame.display.set_caption('Teste1')

    screen.fill([150, 200, 180])
    pygame.draw.line(screen, cores.Cores['CIAN'], [10, 100], [630, 100], 5)
    pygame.draw.rect(screen, cores.Cores['RED'], [obp.p1.X, obp.p1.Y, obp.p1.heigth, obp.p1.width])

    text = font.render(Textos.Textos['Teste'], True, cores.Cores['BLACK'])

    screen.blit(text, [350, 200])
    
    pygame.display.flip()

    time.sleep(5)
    

run = True
while run == True:
    '''
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    '''

    windown()
    
pygame.exit()
