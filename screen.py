import pygame
from constantes import *
from Fondo import *
def inicializar():

  
  pygame.init() 

  reloj = pygame.time.Clock()
  screen = pygame.display.set_mode((ANCHO_VENTANA,LARGO_VENTANA)) #Se crea una ventana
  pygame.display.set_caption("Racing")
  fondo = Fondo("carretera.png")
  x_key_pressed = False

  running = True
  while running:
    #Cerrar
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False 
    
    #si mantiene presionado alguna tecla X avanza 
    lista_key = pygame.key.get_pressed()
        
    if lista_key[pygame.K_x]:
      velocidad = MOV_FONDO 
      #flag para saber si se presiono la tecla x
      x_key_pressed = True

    reloj.tick(FPS)


   
    pygame.display.flip()
  
  pygame.quit() 
