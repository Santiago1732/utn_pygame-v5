import pygame, sys
from settings import *
from level import Level
from data_juego import level_0, level_1
from interfaz import *

class Juego:
    def __init__(self, monedas):
        self.interfaz = Interfaz(screen)
        self.monedas = monedas

    def run(self):
        self.interfaz.mostrar_monedas(1)

    def cambiar_monedas(self,cantidad):
        self.monedas += cantidad

pygame.init()
screen = pygame.display.set_mode((ancho_pantalla, altura_pantalla))
clock = pygame.time.Clock()
level = Level(level_0,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((173, 216, 230))
    level.run()

    pygame.display.update()
    clock.tick(60)