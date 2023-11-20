import pygame, sys
from settings import *
from level import Level
from data_juego import level_0


pygame.init()
screen = pygame.display.set_mode((ancho_pantalla, altura_pantalla))
clock = pygame.time.Clock()
level = Level(level_0,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)