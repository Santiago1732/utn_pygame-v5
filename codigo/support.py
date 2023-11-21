from csv import reader
from settings import tiles_tamaño
import pygame
from os import walk

def importar_csv_layout(path):
    terreno_map = []
    with open(path) as map:
        level = reader(map,delimiter=',')
        for row in level:
            terreno_map.append(list(row))
        return terreno_map

def importar_graficos(path):
    superficie = pygame.image.load(path).convert_alpha()
    tile_num_x = int(superficie.get_size()[0] / tiles_tamaño)
    tile_num_y = int(superficie.get_size()[1] / tiles_tamaño)

    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * tiles_tamaño
            y = row * tiles_tamaño
            nueva_superficie = pygame.Surface((tiles_tamaño,tiles_tamaño), flags = pygame.SRCALPHA)
            nueva_superficie.blit(superficie,(0,0),pygame.Rect(x,y,tiles_tamaño,tiles_tamaño))
            cut_tiles.append(nueva_superficie)

    return cut_tiles

def importar_carpeta(path):
    lista_superficie = []
    for _,__,archivo_imagenes in walk(path):
        for image in archivo_imagenes:
            full_path = path + '/' + image
            image_superficie = pygame.image.load(full_path).convert_alpha()
            lista_superficie.append(image_superficie)

    return lista_superficie