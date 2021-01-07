import random
import funcoes


class personagem():
    def __init__(self, X, Y, heigth, width, velX, velY, eat):
        self.X = X;
        self.Y = Y;
        self.heigth = heigth;
        self.width = width; 
        self.velX = velX;
        self.velY = velY;
        self.eat = eat
        
class apple():
    def __init__(self, X, Y, height, width, velX, velY):
        self.X = X;
        self.Y = Y;
        self.height = height;
        self.width = width;
        self.velX = velX;
        self.velY = velY

p1 = personagem(funcoes.sorteio(), funcoes.sorteio(), 20, 20, 0, 0, 0)
corpo = apple(p1.X - 10, p1.Y - 10, 0, 0, 0, 0)
maca = apple(funcoes.sorteio(), funcoes.sorteio(), 20, 20,  0, 0)
