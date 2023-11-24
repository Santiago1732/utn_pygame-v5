import pygame, sys
from settings import *
from level import Level
from data_juego import level_0, level_1, level_2, levels
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
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)
screen = pygame.display.set_mode((ancho_pantalla, altura_pantalla))
clock = pygame.time.Clock()
# level = Level(level_0,screen)

current_level_index = 0
levels = [level_0, level_1, level_2]
level = Level(levels[current_level_index], screen, current_level_index)


while True:

    if level.cambia_level:
        current_level_index += 1
        if current_level_index >= len(levels):
            current_level_index = 0  # Vuelve al primer nivel o termina el juego
        level = Level(levels[current_level_index], screen,current_level_index)
        level.cambia_level = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    match current_level_index:
        case 0:
            fondo = pygame.image.load('../graficos/terreno/lv-0-fondo.png').convert()
            screen.blit(fondo, (0, 0))
        case 1:
            screen.fill((0, 0, 0))
        case 2:
            screen.fill((175, 253, 255))

    if level.cambia_level:
        level.cambia_level = level.condicion_para_cambiar_de_nivel()
    level.run()
    pygame.display.update()
    clock.tick(60)
