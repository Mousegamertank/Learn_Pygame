import objetos_e_personagens as obp 
import pygame
import random

def funcao_movimento(Key):   
    if Key[pygame.K_LEFT]:
        obp.p1.velY = 0
        obp.p1.velX = -20
        #corpo aux
        obp.corpo.velY = 0
        obp.corpo.velX = -5
        if obp.p1.X <= 0 + obp.p1.width:
            obp.p1.X = 800
            obp.corpo.X = 800
                
    if Key[pygame.K_RIGHT]:
        obp.p1.velY = 0
        obp.p1.velX = 20
        obp.corpo.velY = 0
        obp.corpo.velX = 5
        if obp.p1.X >= 800 - obp.p1.width:
            obp.p1.X = 0
            obp.corpo.X = 0
            
    if Key[pygame.K_UP]:
        obp.p1.velX = 0
        obp.p1.velY = -20
        obp.corpo.velX = 0
        obp.corpo.velY = -5
        if obp.p1.Y <= 0 + obp.p1.width:
            obp.p1.Y = 800
            obp.corpo.Y = 800

    if Key[pygame.K_DOWN]:
        obp.p1.velX = 0
        obp.p1.velY = 20
        obp.corpo.velX = 0
        obp.corpo.velY = 5
        if obp.p1.Y >= 800 - obp.p1.width:
            obp.p1.Y = 0
            obp.corpo.Y = 0
            
def sorteio():
    x = random.randint(0, (800 - 20) / 20) * 20;    
    return x

def colision(Key):
    if obp.p1.X == obp.maca.X and obp.p1.Y == obp.maca.Y:
        obp.maca.X = sorteio()
        obp.maca.Y = sorteio()
        obp.p1.eat += 1
        if obp.p1.eat != 0:
            if Key[pygame.K_LEFT] or Key[pygame.K_RIGHT]:
                obp.corpo.width = 0
                obp.corpo.height = 20 * obp.p1.eat
            
            if Key[pygame.K_UP] or Key[pygame.K_DOWN]:
                obp.corpo.height = 0
                obp.corpo.width = 20 * obp.p1.eat
    
    
