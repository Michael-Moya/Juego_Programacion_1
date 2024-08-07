import pygame
import sys

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 600
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Rebote de Ambos Cuadrados")

# Colores
color_cuadrado1 = (255, 0, 0)  # Rojo
color_cuadrado2 = (0, 0, 255)  # Azul

# Definición de los cuadrados (x, y, ancho, alto)
cuadrado1 = pygame.Rect(100, 100, 100, 100)  # (x, y, width, height)
cuadrado2 = pygame.Rect(200, 150, 100, 100)

# Velocidad de movimiento
velocidad = 5

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mueve el cuadrado 1 con las teclas de flecha
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cuadrado1.x -= velocidad
    if keys[pygame.K_RIGHT]:
        cuadrado1.x += velocidad
    if keys[pygame.K_UP]:
        cuadrado1.y -= velocidad
    if keys[pygame.K_DOWN]:
        cuadrado1.y += velocidad

    # Detección de colisión y rebote
    if cuadrado1.colliderect(cuadrado2):
        # Determinar dirección del movimiento
        if keys[pygame.K_LEFT]:
            cuadrado1.x += velocidad  # Reubicar cuadrado1 hacia la derecha
            cuadrado2.x -= velocidad  # Mover cuadrado2 hacia la izquierda
        if keys[pygame.K_RIGHT]:
            cuadrado1.x -= velocidad  # Reubicar cuadrado1 hacia la izquierda
            cuadrado2.x += velocidad  # Mover cuadrado2 hacia la derecha
        if keys[pygame.K_UP]:
            cuadrado1.y += velocidad  # Reubicar cuadrado1 hacia abajo
            cuadrado2.y -= velocidad  # Mover cuadrado2 hacia arriba
        if keys[pygame.K_DOWN]:
            cuadrado1.y -= velocidad  # Reubicar cuadrado1 hacia arriba
            cuadrado2.y += velocidad  # Mover cuadrado2 hacia abajo

    # Llenar la pantalla con blanco
    screen.fill((255, 255, 255))

    # Dibujar los cuadrados
    pygame.draw.rect(screen, color_cuadrado1, cuadrado1)
    pygame.draw.rect(screen, color_cuadrado2, cuadrado2)

    # Actualizar la pantalla
    pygame.display.flip()
