import pygame
import sys
import random

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 600
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Movimiento Aleatorio de un Cuadrado")

# Colores
color_cuadrado = (255, 0, 0)  # Rojo

# Definición del cuadrado (x, y, ancho, alto)
cuadrado = pygame.Rect(100, 100, 100, 100)

# Velocidad de movimiento
velocidad = 5

# Variables para dirección
direccion_x = random.choice([-1, 1])
direccion_y = random.choice([-1, 1])

# Bucle principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento aleatorio del cuadrado
    cuadrado.x += direccion_x * velocidad
    cuadrado.y += direccion_y * velocidad

    # Comprobar colisiones con los bordes de la pantalla
    if cuadrado.left < 0 or cuadrado.right > ancho:
        direccion_x *= -1  # Cambiar la dirección horizontal
    if cuadrado.top < 0 or cuadrado.bottom > alto:
        direccion_y *= -1  # Cambiar la dirección vertical

    # Llenar la pantalla con blanco
    screen.fill((255, 255, 255))

    # Dibujar el cuadrado
    pygame.draw.rect(screen, color_cuadrado, cuadrado)

    # Actualizar la pantalla
    pygame.display.flip()
    
    # Controlar el framerate
    clock.tick(30)