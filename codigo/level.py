import pygame
from support import importar_csv_layout,importar_graficos
from settings import tiles_tamaño
from tiles import Tile

# level_data: informacion real que nosotros creamos anteriormente en el tilemap
# superficie: superficie de visualizacion de la ventana
class Level:
    def __init__(self, level_data, superficie):
        self.superficie_visualizacion = superficie
        self.mundo_shift = -3
        # Obtengo el mapa tererno (para asegurarnos de que estamos viendo los grafisoc
        # del terreno (porque las monedas pueden tener el mismo id
        mapa_terreno = importar_csv_layout(level_data['terreno'])
        self.terreno_sprites = self.crear_grupo_tiles(mapa_terreno, 'terreno')

    # construir un bucle que circuloe a traves de 'mapa terreno'
    def crear_grupo_tiles(self,layout,tipo):
        grupo_sprites = pygame.sprite.Group()

        for fila_index, fila in enumerate(layout):
            for columna_index, val in enumerate(fila):
                if val != '-1':
                    x = columna_index * tiles_tamaño
                    y = fila_index * tiles_tamaño

                    if tipo == 'terreno':
                        lista_mosaicos_terreno = importar_graficos('../graficos/terreno/terreno.png')
                        sprite = Tile(tiles_tamaño,x,y)
                        grupo_sprites.add(sprite)

        return grupo_sprites

    # corre todo el juego, esto es para no csorrer toda la logica
    # del juego en el main
    def run(self):
        self.terreno_sprites.draw(self.superficie_visualizacion)
        self.terreno_sprites.update(self.mundo_shift)
        pass

