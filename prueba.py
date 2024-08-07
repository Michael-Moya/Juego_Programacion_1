import pygame
from constantes import *
from Fondo import *
from auto import * 
from auto_principal import *
from funciones import *
from instacia_objetos import*

pygame.init() 
pygame.display.set_caption("Racing")
while cerrar_ventana():
  if not juego_pausado:
    if random.randint(1, 100) == 1:  # Ajustar la frecuencia de generación
      charcos = generar_charcos(charcos, avance) 

  avance = iniciar_movimiento_juego(ventana, fondo, auto_principal, avance, auto_cpu, charcos)
  fundir_todo(ventana, fondo, auto_principal, auto_cpu, charcos)
  pygame.display.flip()
  reloj.tick(FPS)
pygame.quit() 

"""try:
    persona.edad = -5
except ValueError as e:
    print(e) 
    """  
