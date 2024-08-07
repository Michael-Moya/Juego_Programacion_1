import pygame
import random
from constantes import *
from auto import *
class Charco() :
  def __init__(self , speed) -> None:
    self.superficie = self.__crear_charco("charco.png")
    self.speed = speed
    self.rect = self.superficie.get_rect()
    
    self.posicion = self.__posicionar()
    self.rect.topleft = self.posicion
    self.visible = True
    self.color_rect = COLOR_RECT_CHARCO
  def mover(self,velocidad):
    self.speed = velocidad
    self.rect.y = self.rect.y + self.speed

  def mover_desacelerado(self,avance):
    if avance < 0.3:
      return False
    else:
      self.mover(avance)
      return True
  
  def colisionar(self , auto ):
    flag = False
    if auto.rect.colliderect(self.rect):
      self.visible = False
      flag = True
    return flag
#considerar a eliminar
  def update_mover_charco(self, velocidad, movimiento = True):
    if movimiento:
      self.mover(velocidad)
    else:
      self.mover_desacelerado(velocidad)

  def __crear_charco(self,path):
    imagen_charco = pygame.image.load(path)
    imagen_charco = pygame.transform.scale(imagen_charco,(200,200))
    return imagen_charco
  def __posicionar(self):
    lista= []
    y = random.randrange(-900,0,50)
    x = random.randrange(80,720,60)   
    lista = [x,y] 
    return lista

  def dibujar(self, pantalla):
    if self.visible:
      pantalla.blit(self.superficie,self.rect)
    pygame.draw.rect(pantalla, self.color_rect, self.rect)