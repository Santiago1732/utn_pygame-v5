import codigo.bdd
from settings import *
from level import Level
from data_juego import level_0, level_1, level_2
from UI import *
from menu import *
from bdd import crear_db, insertar_jugador

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((ancho_pantalla, altura_pantalla))
clock = pygame.time.Clock()
nombre_jugador = None
# level = Level(level_0,screen)
# sonido_activado = True
menu = main_menu(Menu)

if menu is not None:

    crear_db()
    current_level_index = 0

    levels = [level_0, level_1, level_2]
    level = Level(levels[current_level_index], screen, current_level_index)
    ui = UI(screen)

    if menu.sonido_activado:
        level.reproducir_sonido(current_level_index)

    while True:
        if not level.vivo:
            current_level_index -= 1
            level.vivo = True

            level = Level(levels[current_level_index], screen, current_level_index)
            level.cambia_level = False

        if level.cambia_level:

            level.apagar_sonido(current_level_index)

            current_level_index += 1
            if current_level_index >= len(levels):
                current_level_index = 0

            if menu.sonido_activado:
                level.reproducir_sonido(current_level_index)

            level = Level(levels[current_level_index], screen,current_level_index)
            level.cambia_level = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tiempo_transcurrido = pygame.time.get_ticks()
                tiempo_en_segundos = tiempo_transcurrido / 1000
                tiempo_en_minutos = tiempo_en_segundos / 60

                tiempo_total = f"{tiempo_en_minutos}:,{tiempo_en_segundos}"

                insertar_jugador(menu.nombre_jugador,current_level_index,tiempo_total)
                pygame.quit()
                sys.exit()

        match current_level_index:
            case 0:
                ui.mostrar_monedas(level.cambiar_monedas)
                fondo = pygame.image.load('../graficos/terreno/lv-0-fondo.png').convert()
                screen.blit(fondo, (0, 0))
            case 1:
                ui.mostrar_monedas(level.cambiar_monedas)
                fondo = pygame.image.load('../graficos/terreno/infierno.jpg').convert()
                screen.blit(fondo,(0,0))
                # screen.fill((0, 0, 0))
            case 2:
                ui.mostrar_monedas(level.cambiar_monedas)
                screen.fill((14, 22, 51))

        if level.cambia_level:
            level.cambia_level = level.condicion_para_cambiar_de_nivel()
        level.run()
        pygame.display.update()
        clock.tick(60)
