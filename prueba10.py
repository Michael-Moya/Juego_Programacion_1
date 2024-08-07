import pygame
import random

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Carrera de cuadrados")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Parámetros de los cuadrados
size = 50
square1_pos = [100, HEIGHT // 2 - size // 2]  # Cuadrado controlado por el jugador
square2_pos = [WIDTH - 150, HEIGHT // 2 - size // 2]  # Cuadrado que se mueve solo
square1_speed = 5
square2_speed = 5

# Variables para la dirección de movimiento
square2_direction = -1  # -1 significa a la izquierda

# Reloj para controlar los FPS
clock = pygame.time.Clock()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movimiento del cuadrado controlado por el jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        square1_pos[0] -= square1_speed
    if keys[pygame.K_RIGHT]:
        square1_pos[0] += square1_speed

    # Movimiento del cuadrado azul
    square2_pos[0] += square2_speed * square2_direction

    # Colisión entre los cuadrados
    if (square1_pos[0] < square2_pos[0] + size and
        square1_pos[0] + size > square2_pos[0] and
        square1_pos[1] < square2_pos[1] + size and
        square1_pos[1] + size > square2_pos[1]):
        
        # Separar los cuadrados ligeramente
        if square1_pos[0] < square2_pos[0]:
            square1_pos[0] = square2_pos[0] - size  # Mover el cuadrado rojo a la izquierda
        else:
            square1_pos[0] = square2_pos[0] + size  # Mover el cuadrado rojo a la derecha

        # Rebote en direcciones opuestas sin invertir el control del jugador
        square2_direction *= -1

    # Limitar el cuadrado controlado por el jugador dentro de la ventana
    if square1_pos[0] < 0:
        square1_pos[0] = 0
    if square1_pos[0] + size > WIDTH:
        square1_pos[0] = WIDTH - size

    # Limitar el cuadrado azul dentro de la ventana
    if square2_pos[0] < 0 or square2_pos[0] + size > WIDTH:
        square2_direction *= -1

    # Dibujar en la ventana
    window.fill(WHITE)
    pygame.draw.rect(window, RED, (*square1_pos, size, size))  # Cuadrado rojo (controlado por el jugador)
    pygame.draw.rect(window, BLUE, (*square2_pos, size, size))  # Cuadrado azul (movimiento automático)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
