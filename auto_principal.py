import pygame
from auto import *
from constantes import *
from auto_cpu import *

#timer_event = pygame.USEREVENT + 1  # Crear un nuevo evento
#pygame.time.set_timer(timer_event, 300)  # Evento cada 1000 ms (1 segundo)
class AutoPrincipal(Auto) :
  def __init__(self)-> None:
    super().__init__("auto_amarillo.jpg")
    self.rect = self.imagen_normal.get_rect()
    self.rect.topleft = [400,400]
    self.posicion_real = self.posicionar()
    self.rect.width = 100
    self.rect.height = 200
    self.color_rect = COLOR_RECT_AUTO

  def mover(self, incremento):
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_x]:
      self.__direccionar()
      movimiento = self.__avanzar_o_retroceder()
      self.__avanzar_posicion_relativa(incremento, movimiento)
      self.posicion_real = self.posicionar()

  def __direccionar(self):
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_RIGHT]:
      self.rect.x += 3
    elif keys[pygame.K_LEFT] :
      self.rect.x -= 3
    self.limitar_posicion_por_ventana()

  def __avanzar_o_retroceder(self)->int:
    movimiento = 0
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_UP]:
      self.rect.y -= 2
      movimiento = 2
    elif keys[pygame.K_DOWN]:
      self.rect.y += 2   
      movimiento = -2   
    return movimiento

  def __avanzar_posicion_relativa(self, incremento:int, movimiento:int):
    self.posicion_relativa[1] = self.posicion_relativa[1] + incremento + movimiento
    self.posicion_relativa[0] = self.rect.x

  def __get_superficie(self, path, filas, columnas) -> list:
    lista = []
    superfice_imagen = pygame.image.load(path)
    fotograma_ancho = int(superfice_imagen.get_width()/columnas)
    fotograma_alto = int(superfice_imagen.get_height()/filas)
    for fila in range(filas):
      for columna in range(columnas ):
        x = columna * fotograma_ancho
        y = fila *  fotograma_alto
        #un pedazo de la superficie
        superficie_fotograma = superfice_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
        lista.append(superficie_fotograma)
    return lista
  


        # Rebote en direcciones opuestas sin invertir el control del jugador
        #auto_cpu.rect *= -1
