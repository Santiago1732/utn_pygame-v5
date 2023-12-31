import pygame
import sys

class Menu():
    def __init__(self, nombre_jugador, sonido_activado):
        super().__init__()
        self.nombre_jugador = nombre_jugador
        self.sonido_activado = sonido_activado


# Inicializar Pygame
pygame.init()

# Configuraciones de la ventana
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Santiago Oliveira - UTN - TP Pygame ')

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuente
font = pygame.font.Font(None, 36)

# Funciones para cada pantalla
def main_menu(self):
    menu = Menu('None',True)
    sonido_activado = True
    nombre_jugador = ''
    while True:
        screen.fill(WHITE)
        draw_text('Main Menu', font, BLACK, screen, 20, 20)
        draw_text('1. Jugar', font, BLACK, screen, 20, 100)
        draw_text('2. Opciones', font, BLACK, screen, 20, 140)
        draw_text('3. Salir', font, BLACK, screen, 20, 180)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:

                    # NOMBRE JUGADOR
                    case pygame.K_1:
                        menu.nombre_jugador = game_screen(sonido_activado)
                        return menu

                    # OPCIONES
                    case pygame.K_2:
                        menu.sonido_activado = options_screen()

                    # SALIR
                    case pygame.K_3:
                        pygame.quit()
                        sys.exit()

        pygame.display.update()


def game_screen(self, sonido_activado = True):
    running = True
    while running:
        screen.fill(WHITE)
        player_name = text_input()

        if player_name is not None:
            return player_name

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.nombre_jugador = game_screen(sonido_activado)
                    pygame.display.update()


sonido_activado = True
def options_screen():
    global sonido_activado  # Usar la variable global

    while True:
        screen.fill(WHITE)
        draw_text(' - OPCIONES- ', font, BLACK, screen, 20, 20)
        draw_text('2) Atras', font, BLACK, screen, 20, 140)

        if sonido_activado:
            draw_text('1) Desactivar Sonido', font, BLACK, screen, 20, 100)
        else:
            draw_text('1) Activar Sonido', font, BLACK, screen, 20, 100)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    sonido_activado = not sonido_activado
                elif event.key == pygame.K_2:
                    return sonido_activado

        pygame.display.update()


def text_input():
    nombre_jugador = ''
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if event.type == pygame.K_ESCAPE:
            #     main_menu()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = True
                    return nombre_jugador

                elif event.key == pygame.K_ESCAPE:
                    main_menu()
                elif event.key == pygame.K_BACKSPACE:
                    nombre_jugador = nombre_jugador[:-1]
                else:
                    nombre_jugador += event.unicode

        screen.fill(WHITE)
        draw_text("Ingrese su nombre:", font, BLACK, screen, 20, 20)
        draw_text(nombre_jugador, font, BLACK, screen, 20, 80)

        draw_text('Enter) Jugar:', font, BLACK, screen, 20, 100)
        pygame.display.flip()

    return nombre_jugador


# Función para dibujar texto
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# Bucle principal
def main():
    while True:
        main_menu()


if __name__ == '__main__':
    main()
