import pygame
from support import importar_csv_layout,importar_graficos
from settings import tiles_tamaño
from tiles import Tile, StaticTile
from enemigo import Enemigo
from player import Player
from settings import *

# level_data: informacion real que nosotros creamos anteriormente en el tilemap
# superficie: superficie de visualizacion de la ventana
class Level:
    def __init__(self, level_data, superficie):
        self.superficie_visualizacion = superficie
        self.mundo_shift = 0
        self.x_actual = None

       # PL AYER
        mapa_player = importar_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.player_setup(mapa_player)

        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(mapa_player)

        # Obtengo el mapa tererno (para asegurarnos de que estamos viendo los grafisoc
        # del terreno (porque las monedas pueden tener el mismo id
        mapa_terreno = importar_csv_layout(level_data['terreno'])
        self.terreno_sprites = self.crear_grupo_tiles(mapa_terreno, 'terreno')

        mapa_monedas = importar_csv_layout(level_data['monedas'])
        self.modenas_sprites = self.crear_grupo_tiles(mapa_monedas,'monedas')

        mapa_enemigo = importar_csv_layout(level_data['enemigo'])
        self.enemigo_sprites = self.crear_grupo_tiles(mapa_enemigo,'enemigo')

        # reestricciones
        mapa_reestricciones = importar_csv_layout(level_data['reestricciones'])
        self.reestricciones_sprites = self.crear_grupo_tiles(mapa_reestricciones,'reestricciones')

    # construir un bucle que circuloe a traves de 'mapa terreno'
    def crear_grupo_tiles(self,layout,tipo):
        grupo_sprites = pygame.sprite.Group()

        for fila_index, fila in enumerate(layout):
            for columna_index,val in enumerate(fila):
                if val != '-1':
                    x = columna_index * tiles_tamaño
                    y = fila_index * tiles_tamaño

                    if tipo == 'terreno':
                        lista_mosaicos_terreno = importar_graficos('../graficos/terreno/fondoTerreno.png')
                        tile_superficie = lista_mosaicos_terreno[int(val)]
                        sprite = StaticTile(tiles_tamaño,x,y,tile_superficie)
                        grupo_sprites.add(sprite)

                    if tipo == 'monedas':
                        lista_mosaicos_monedas = importar_graficos('../graficos/monedas/Coins-PNG.png')
                        tile_superficie = lista_mosaicos_monedas[int(val)]
                        sprite = StaticTile(tiles_tamaño,x,y,tile_superficie)
                        grupo_sprites.add(sprite)

                    if tipo == 'enemigo':
                        sprite = Enemigo(tiles_tamaño,x,y)

                    if tipo == 'reestricciones':
                        sprite = Tile(tiles_tamaño,x,y)


                    grupo_sprites.add(sprite)

        return grupo_sprites

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direccion_x = player.direction.x

        if player_x < ancho_pantalla / 4 and direccion_x < 0:
            self.mundo_shift = 8
            player.speed = 0
        elif player_x > ancho_pantalla - (ancho_pantalla / 4) and direccion_x > 0:
            self.mundo_shift = -8
            player.speed = 0
        else:
            self.mundo_shift = 0
            player.speed = 8

    def player_setup(self,layout):
        for fila_index, fila in enumerate(layout):
            for columna_index, val in enumerate(fila):
                x = columna_index * tiles_tamaño
                y = fila_index * tiles_tamaño
                if val == '0':
                    sprite = Player((x,y),self.superficie_visualizacion)
                    self.player.add(sprite)
                if val == '1':
                    # REVISAR QUE HACER CON ESTO
                    algo_superficie = pygame.image.load('../graficos/character/inactivo/6.png').convert_alpha()
                    sprite = StaticTile(tiles_tamaño,x,y,algo_superficie)
                    self.goal.add(sprite)

    def horizontal_movement_colission(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        print(player.rect.x)
        for sprite in self.terreno_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.a_la_derecha = True
                    self.x_actual = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.a_la_izquierda = True
                    self.x_actual = player.rect.right

        if player.a_la_izquierda and (player.rect.left < self.x_actual or player.direction.x >= 0):
            player.a_la_izquierda = False
        if player.a_la_derecha and (player.rect.right < self.x_actual or player.direction.x <= 0):
            player.a_la_derecha = False
    def vertical_movement_colission(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.terreno_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                # EN EL PISO
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.en_el_piso = True

                    # EN EL TECHO
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.en_el_techo = True

        if player.en_el_piso and player.direction.y < 0 or player.direction.y > 1:
            player.en_el_piso = False
        if player.en_el_techo and player.direction.y > 0:
            player.en_el_techo = False
    def enemigo_colission_reversa(self):
        for enemigo in self.enemigo_sprites.sprites():
            if pygame.sprite.spritecollide(enemigo,self.terreno_sprites,False):
                enemigo.reversa()

    # corre todo el juego, esto es para no csorrer toda la logica
    # del juego en el main
    def run(self):

        # TERRENO
        self.terreno_sprites.draw(self.superficie_visualizacion)
        self.terreno_sprites.update(self.mundo_shift)
        self.scroll_x()

        # MONEDAS
        self.modenas_sprites.draw(self.superficie_visualizacion)
        self.modenas_sprites.update(self.mundo_shift)

        # ENEMIGO
        self.enemigo_sprites.update(self.mundo_shift)
        self.reestricciones_sprites.update(self.mundo_shift)
        self.enemigo_colission_reversa()
        self.enemigo_sprites.draw(self.superficie_visualizacion)

        # PLAYER
        self.player.update()
        self.horizontal_movement_colission()
        self.vertical_movement_colission()
        self.scroll_x()
        self.player.draw(self.superficie_visualizacion)

        pass

