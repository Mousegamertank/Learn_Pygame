import objetos_e_personagens as obp 
import pygame
import random

def funcao_movimento(Key):   
    if Key[pygame.K_LEFT]:
        obp.p1.velY = 0
        obp.p1.velX = -20
        if obp.p1.X < 0:
            obp.p1.X = 800
                
    if Key[pygame.K_RIGHT]:
        obp.p1.velY = 0
        obp.p1.velX = 20
        if obp.p1.X > 800:
            obp.p1.X = 0
            
    if Key[pygame.K_UP]:
        obp.p1.velX = 0
        obp.p1.velY = -20
        if obp.p1.Y < 0:
            obp.p1.Y = 800

    if Key[pygame.K_DOWN]:
        obp.p1.velX = 0
        obp.p1.velY = 20
        if obp.p1.Y > 800:
            obp.p1.Y = 0
            
def sorteio():
    x = random.randint(0, (800 - 20) / 10) * 10;    
    return x

  
