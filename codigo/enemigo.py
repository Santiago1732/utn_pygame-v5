import pygame
from tiles import TileAnimada
from random import randint

class Enemigo(TileAnimada):
    def __init__(self,tamaño,x,y):
        super().__init__(tamaño,x,y,'../graficos/enemigo/corriendo')
        self.rect.y += tamaño - self.image.get_size()[1]
        self.velocidad = randint(3,5)

    def movimiento(self):
        self.rect.x -= self.velocidad

    def imagen_reversa(self):
        if self.velocidad > 0:
            self.image = pygame.transform.flip(self.image,True,False)


    def reversa(self):
        self.velocidad *= -1


    def update(self,shift):
        self.rect.x += shift
        self.animar()
        self.movimiento()
        self.imagen_reversa()