import objetos_e_personagens as obp 
import pygame
import random

def funcao_movimento(Key):
    if obp.p1.velX == 0 and obp.p1.velX == 0:
        inicio = iniciar()
        if inicio == 0: 
            obp.p1.velY = 0
            obp.p1.velX = -20
        elif inicio == 1:
            obp.p1.velY = 0
            obp.p1.velX = 20
        elif inicio == 2:
            obp.p1.velY = 20
            obp.p1.velX = 0
        else:
            obp.p1.velY = -20
            obp.p1.velX = 0

            
    if Key[pygame.K_LEFT]:
        if obp.p1.velY != 0 or obp.p1.velX != 20:
            obp.p1.velY = 0
            obp.p1.velX = -20
            #corpo aux
            obp.corpo.velY = 0
            obp.corpo.velX = -5
            if obp.p1.X <= 0 + obp.p1.width:
                obp.p1.X = 800
                obp.corpo.X = 800
        else:
            pass
                
    if Key[pygame.K_RIGHT]:
        if obp.p1.velY != 0 or obp.p1.velX != -20:
            obp.p1.velY = 0
            obp.p1.velX = 20
            obp.corpo.velY = 0
            obp.corpo.velX = 5
            if obp.p1.X >= 800 - obp.p1.width:
                obp.p1.X = 0
                obp.corpo.X = 0
        else:
            pass
            
    if Key[pygame.K_UP]:
        if obp.p1.velY != 20 or obp.p1.velX != 0:
            obp.p1.velX = 0
            obp.p1.velY = -20
            obp.corpo.velX = 0
            obp.corpo.velY = -5
            if obp.p1.Y <= 0 + obp.p1.width:
                obp.p1.Y = 800
                obp.corpo.Y = 800
        else:
            pass

    if Key[pygame.K_DOWN]:
        if obp.p1.velY != -20 or obp.p1.velX != 0:
            obp.p1.velX = 0
            obp.p1.velY = 20
            obp.corpo.velX = 0
            obp.corpo.velY = 5
            if obp.p1.Y >= 800 - obp.p1.width:
                obp.p1.Y = 0
                obp.corpo.Y = 0
        else:
            pass
            
def sorteio():
    x = random.randint(0, (800 - 20) / 20) * 20;    
    return x

def colision():
    if obp.p1.X == obp.maca.X and obp.p1.Y == obp.maca.Y:
        obp.maca.X = sorteio()
        obp.maca.Y = sorteio()
        obp.p1.eat += 1
            

def mostrarCorpo():
    if obp.p1.eat != 0:
        if obp.p1.velY == 0 and obp.p1.velX != 0:
            passado_X = obp.p1.velX - (20 * obp.p1.eat)
            return passado_X
        else:
            passado_Y = obp.p1.velY - (20 * obp.p1.eat)
            return passado_Y

def iniciar ():
    Key = pygame.key.get_pressed()
    if Key[pygame.K_KP_ENTER]:
        return random.randint(0, 4)
