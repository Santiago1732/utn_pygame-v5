import pygame
from tiles import TileAnimada

class Enemigo(TileAnimada):
    def __init__(self,tamaño,x,y):
        super().__init__(tamaño,x,y,'../graficos/enemigo/corriendo')