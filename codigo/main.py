import pygame, sys
from settings import *
from level import Level
from data_juego import level_0, level_1, level_2, levels
from interfaz import *
from UI import *

pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(1.0)
screen = pygame.display.set_mode((ancho_pantalla, altura_pantalla))
clock = pygame.time.Clock()
# level = Level(level_0,screen)

current_level_index = 2
levels = [level_0, level_1, level_2]
level = Level(levels[current_level_index], screen, current_level_index)
ui = UI(screen)

while True:
    if not level.vivo:
        current_level_index -= 1
        level.vivo = True

        level = Level(levels[current_level_index], screen, current_level_index)
        level.cambia_level = False

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
            ui.mostrar_monedas(level.cambiar_monedas)
            fondo = pygame.image.load('../graficos/terreno/lv-0-fondo.png').convert()
            screen.blit(fondo, (0, 0))
        case 1:
            ui.mostrar_monedas(level.cambiar_monedas)
            screen.fill((0, 0, 0))
        case 2:
            ui.mostrar_monedas(level.cambiar_monedas)
            screen.fill((14, 22, 51))

    if level.cambia_level:
        level.cambia_level = level.condicion_para_cambiar_de_nivel()
    level.run()
    pygame.display.update()
    clock.tick(60)
