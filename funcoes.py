import objetos_e_personagens as obp 
import pygame
import random
import Textos
import cores

def funcao_movimento(Key, font, screen):            
    if Key[pygame.K_LEFT]:
        if obp.p1.velY != 0 or obp.p1.velX != 20:
            obp.p1.velY = 0
            obp.p1.velX = -20
            if obp.p1.X <= 0 + obp.p1.width:
                perdeu(font, screen)
        else:
            pass
                
    if Key[pygame.K_RIGHT]:
        if obp.p1.velY != 0 or obp.p1.velX != -20:
            obp.p1.velY = 0
            obp.p1.velX = 20 
            if obp.p1.X >= 800 - obp.p1.width:
                perdeu(font, screen)
        else:
            pass
            
    if Key[pygame.K_UP]:
        if obp.p1.velY != 20 or obp.p1.velX != 0:
            obp.p1.velX = 0
            obp.p1.velY = -20
            if obp.p1.Y <= 0:
                perdeu(font, screen)
        else:
            pass

    if Key[pygame.K_DOWN]:
        if obp.p1.velY != -20 or obp.p1.velX != 0:
            obp.p1.velX = 0
            obp.p1.velY = 20
        if obp.p1.Y >= 800 - obp.p1.width:
            perdeu(font, screen)

            
def sorteio():
    x = random.randint(0, (800 - 20) / 20) * 20;    
    return x

def colision():
    if obp.p1.X == obp.maca.X and obp.p1.Y == obp.maca.Y:
        obp.maca.X = sorteio()
        obp.maca.Y = sorteio()
        obp.p1.eat += 1

def perdeu():
    run = True
    if obp.p1.X < 0 or obp.p1.X > 800 or obp.p1.Y < 0 or obp.p1.Y > 800:
        run = False
    return run

def restart():
    

