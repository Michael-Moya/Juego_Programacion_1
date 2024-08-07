import pygame
import sys
import random

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 400, 600
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Movimiento Aleatorio de un Cuadrado Hacia Arriba")

# Colores
color_cuadrado = (255, 0, 0)  # Rojo

# Definición del cuadrado (x, y, ancho, alto)
cuadrado = pygame.Rect(100, 500, 100, 100)  # Comienza en el centro de la parte inferior

# Velocidad de movimiento
velocidad_vertical = 5
velocidad_horizontal = 3

# Variables para movimiento horizontal
direccion_horizontal = 1  # 1 = derecha, -1 = izquierda
tiempo_cambio_direccion = 30  # Tiempo en frames antes de cambiar de dirección
frames_hasta_cambio = tiempo_cambio_direccion

# Bucle principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento vertical hacia arriba
    cuadrado.y -= velocidad_vertical

    # Movimiento horizontal
    cuadrado.x += direccion_horizontal * velocidad_horizontal

    # Contar los frames hasta el próximo cambio de dirección
    frames_hasta_cambio -= 1
    if frames_hasta_cambio <= 0:
        # Cambiar dirección
        direccion_horizontal *= -1  # Cambiar la dirección
        frames_hasta_cambio = tiempo_cambio_direccion  # Reiniciar el contador

    # Restringir el movimiento horizontal para que no se salga de la pantalla
    if cuadrado.left < 0:
        cuadrado.left = 0  # Limitar al borde izquierdo
        direccion_horizontal = 1  # Cambiar dirección hacia la derecha
    if cuadrado.right > ancho:
        cuadrado.right = ancho  # Limitar al borde derecho
        direccion_horizontal = -1  # Cambiar dirección hacia la izquierda

    # Comprobar si el cuadrado sale de la parte superior de la pantalla
    if cuadrado.top < 0:
        cuadrado.top = 0  # Si el cuadrado sale de la pantalla por la parte superior

    # Llenar la pantalla con blanco
    screen.fill((255, 255, 255))

    # Dibujar el cuadrado
    pygame.draw.rect(screen, color_cuadrado, cuadrado)

    # Actualizar la pantalla
    pygame.display.flip()
    
    # Controlar el framerate
    clock.tick(30)
