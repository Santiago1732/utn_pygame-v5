import pygame, sys
from settings import *
from level import Level
from data_juego import level_0
from interfaz import *

class Juego:
    def __init__(self):
        self.monedas = 0
        self.interfaz = Interfaz(screen)

    def run(self):
        self.interfaz.mostrar_monedas()

pygame.init()
screen = pygame.display.set_mode((ancho_pantalla, altura_pantalla))
clock = pygame.time.Clock()
level = Level(level_0,screen)
juego = Juego()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 255, 255))
    level.run()
    juego.interfaz.mostrar_monedas('12')

    pygame.display.update()
    clock.tick(60)