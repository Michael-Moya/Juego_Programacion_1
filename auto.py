import pygame
from abc import ABC, abstractmethod
from colores import *
from constantes import *
from charco import *
import time
class Auto(ABC) :
  def __init__(self,path) -> None:
    self.lados = self.__get_superficie(path,1,3)
    self.imagen_normal = self.lados[1]

    self.posicion_relativa = [0 , 0]
    self.color_rect = AQUAMARINE1

    self.is_stabilizing = False
    self.start_time = 0
    self.cont_desestabilizacion = 0
    
  def limitar_posicion_por_ventana(self):
    if self.rect.left < 0 :
      self.rect.x = 0
    elif self.rect.right > ANCHO_VENTANA:
      self.rect.right = ANCHO_VENTANA  
  
  def posicionar(self):
    return [self.rect.x-47, self.rect.y-33]
  
  def administrar_colision(self):
    if self.cont_desestabilizacion < 2:
      self.desestabilizar()
    
  def desestabilizar(self):
    self.is_stabilizing = True
    self.cont_desestabilizacion +=1 
    self.start_time = pygame.time.get_ticks()

      # Registra el tiempo de inicio

  def controlar_la_desestabilización(self):
    if self.is_stabilizing:
      tiempo_actual = pygame.time.get_ticks()
      tiempo_diferencia = tiempo_actual - self.start_time
      print(tiempo_diferencia)
      print("--------------")
      if tiempo_diferencia <= 300 :  # 300 ms de desestabilización
        self.imagen_normal = self.lados[0]  # Mueve el objet o a la derecha
      elif tiempo_diferencia > 300 and tiempo_diferencia < 1000  :
        print("paso por cambio")
        self.imagen_normal = self.lados[2] 
      else:
        self.is_stabilizing = False
    else:       
        self.imagen_normal = self.lados[1] # Regresa a la posición original
        self.cont_desestabilizacion = 0
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
  @abstractmethod  
  def mover(self, incremento):
    pass
  def dibujar(self, pantalla):
    pantalla.blit(self.imagen_normal,(self.posicion_real,(self.rect.width, self.rect.height )))
    pygame.draw.rect(pantalla, self.color_rect, self.rect)

  







