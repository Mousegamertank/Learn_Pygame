import random
import funcoes

class personagem():
    def __init__(self, X, Y, heigth, width, velX, velY):
        self.X = X
        self.Y = Y
        self.heigth = heigth
        self.width = width
        self.velX = velX
        self.velY = velY

p1 = personagem(funcoes.sorteio(), funcoes.sorteio(), 20, 20, 0, 0)
maca = personagem(funcoes.sorteio(), funcoes.sorteio(), 20, 20, 0, 0)
