from csv import reader
from settings import tiles_tamaño
import pygame

def importar_csv_layout(path):
    terreno_map = []
    with open(path) as map:
        level = reader(map,delimiter= ',')
        for row in level:
            terreno_map.append(list(row))
        return terreno_map

def importar_graficos(path):
    superficie = pygame.image.load(path).convert_alpha()
    tile_num_x = int(superficie.get_size()[0] / tiles_tamaño)
    tile_num_y = int(superficie.get_size()[1] / tiles_tamaño)

    cut_tiles = []
    for row in range(tile_num_x):
        for col in range(tile_num_y):
            x = col * tiles_tamaño
            y = row * tiles_tamaño
            nueva_superficie = pygame.Surface((tiles_tamaño,tiles_tamaño))
            nueva_superficie.blit(superficie,(x,y),pygame.Rect(x,y,tiles_tamaño,tiles_tamaño))
            cut_tiles.append(nueva_superficie)

    return cut_tiles