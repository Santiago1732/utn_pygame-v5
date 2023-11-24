import pygame
from codigo.support import importar_carpeta

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, superficie):
        super().__init__()
        self.importar_imagenes()
        self.imagen_index = 0
        self.velocidad_animacion = 0.15
        self.image = self.animaciones['inactivo'][self.imagen_index]
        self.rect = self.image.get_rect(topleft=pos)

        # movimiento player
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        # self.superficie_visualiazcion = superficie

        self.cara_derecha = True
        self.en_el_piso = False
        self.en_el_techo = False
        self.a_la_derecha = False
        self.a_la_izquierda = False

        self.cantidad_monedas = 0
        self.vivo = True

    def importar_imagenes(self):
        imagenes_path = '../graficos/character/'
        self.animaciones  = {'inactivo':[], 'saltando':[], 'corriendo':[],'cayendo':[]}

        for animacion in self.animaciones.keys():
            path_completo = imagenes_path + animacion
            self.animaciones[animacion] = importar_carpeta(path_completo)

    def animar(self):
        animacion = self.animaciones[self.estado]

        # loop por cada index
        self.imagen_index += self.velocidad_animacion
        if self.imagen_index >= len(animacion):
            self.imagen_index = 0

        imagen = animacion[int(self.imagen_index)]
        if self.cara_derecha:
            # CHEQUEAR
            self.image = imagen
        else:
            flipped_image = pygame.transform.flip(imagen,True,False)
            self.image = flipped_image

        if self.en_el_piso and self.a_la_derecha:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.en_el_piso and self.a_la_izquierda:
            self.rect = self.image.get_rect(bottomleft=self.rect.bottomleft)
        elif self.en_el_piso:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)

        if self.en_el_techo and self.a_la_derecha:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.en_el_techo and self.a_la_izquierda:
            self.rect = self.image.get_rect(topleft=self.rect.topleft)
        elif self.en_el_piso:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 0.8
            # DIRECCION DE LA CARA
            self.cara_derecha = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -0.8
            # DIRECCION DE LA CARA
            self.cara_derecha = False
        else:
            self.direction.x = 0

        if keys[pygame.K_UP] and self.en_el_piso:
            self.jump()

    # {'inactivo': [], 'saltando': [], 'corriendo': [], 'cayendo': []}
    def obtener_estado(self):
        if self.direction.y < 0:
            self.estado = 'saltando'
        elif self.direction.y > 1:
            self.estado = 'cayendo'
        else:
            if self.direction.x != 0:
                self.estado = 'corriendo'
            else:
                self.estado = 'inactivo'


    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed


    def update(self):
        self.get_input()
        self.obtener_estado()
        self.animar()
