import pygame
from constantes import *
from Fondo import *
from auto import * 
from auto_principal import *
from auto_cpu import *
reloj = pygame.time.Clock()
#Se crea una ventana
ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTURA_VENTANA)) 
# elementos del juego
fondo = Fondo("carretera.png")     
auto_principal = AutoPrincipal()
auto_cpu = AutoCpu(POSICION_INICIAL_CPU)
charcos = []

avance = 0
running = True
juego_pausado = False

# Variables de tiempo
tiempo_inicio = pygame.time.get_ticks()
tiempo_espera = 100  # Tiempo de espera en milisegundos
tiempo_diferencia = 0
