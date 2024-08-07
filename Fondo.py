import pygame
from constantes import *
class Fondo():
  def __init__(self,path) -> None:
    self.posicion = [POSICION_FONDO_X,POSICION_FONDO_Y]
    self.superficie = self.__crear_fondo(path)
    self.imagen = self.superficie
    self.alto = self.imagen.get_rect().height        
  
  def movimiento(self,pantalla, avance):
    y_relativa = self.posicion[1] % self.alto
    self.posicion[1] = y_relativa
    pantalla.blit(self.imagen, (self.posicion[0] ,self.posicion[1]))
    y = (y_relativa-self.alto) 
    #funde el fondo hacia arriba , puede ser mas largo que la ventana pero nunca menor a eso
    if y_relativa < ALTURA_VENTANA:
      pantalla.blit(self.imagen,(self.posicion[0], y))

    #los cambios de la posicion del fondo 
    self.posicion[1] = self.posicion[1] + avance
    
#  def movimiento_desacelerado(self, pantalla, avance):
 #   if avance < 0.3:
 #     return False
 #   else:
#      self.movimiento(pantalla,avance)
 #     return True


  def dibujar(self , pantalla ):
    pantalla.blit(self.imagen,self.posicion)

  def __crear_fondo(self, path:str):
    fondo = pygame.image.load(path)
    fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA,ALTURA_VENTANA))
    return fondo

    

        