import pygame
from support import importar_carpeta

class Tile(pygame.sprite.Sprite):
    def __init__(self,tamaño,x,y):
        super().__init__()
        self.image = pygame.Surface((tamaño,tamaño))
        # self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = (x,y))

    def update(self,shift):
        self.rect.x += shift

class StaticTile(Tile):
    def __init__(self, tamaño,x,y,superficie):
        super().__init__(tamaño,x,y)
        self.image = superficie

class TileAnimada(Tile):
    def __init__(self,tamaño,x,y,path):
        super().__init__(tamaño,x,y)
        self.frames = importar_carpeta(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animar(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self,shift):
        self.animar()
        self.rect.x += shift