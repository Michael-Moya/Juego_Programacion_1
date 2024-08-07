import pygame
import sys
import random

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
ancho, alto = 800, 600
screen = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Carrera de Cuadrados")

# Colores
color_jugador = (255, 0, 0)  # Rojo para el jugador
color_automatico = (0, 0, 255)  # Azul para el cuadrado automático
color_meta = (0, 255, 0)  # Verde para la línea de meta

# Definición de los cuadrados
cuadrado_jugador = pygame.Rect(100, alto - 120, 50, 50)  # Cuadrado del jugador
cuadrado_automatico = pygame.Rect(300, alto - 120, 50, 50)  # Cuadrado automático

# Velocidades de movimiento
velocidad_jugador = 5
velocidad_automatico = 3

# Bucle principal
clock = pygame.time.Clock()
ganador = None

# Línea de meta
linea_meta_y = 50  # Posición Y de la línea de meta

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        cuadrado_jugador.x -= velocidad_jugador
    if keys[pygame.K_RIGHT]:
        cuadrado_jugador.x += velocidad_jugador

    # Restringir movimiento del jugador
    if cuadrado_jugador.left < 0:
        cuadrado_jugador.left = 0
    if cuadrado_jugador.right > ancho:
        cuadrado_jugador.right = ancho

    # Movimiento aleatorio del cuadrado automático
    if random.random() < 0.5:  # Hay una probabilidad de 50% de moverse a la izquierda o derecha
        cuadrado_automatico.x += velocidad_automatico
    else:
        cuadrado_automatico.x -= velocidad_automatico

    # Restringir movimiento del cuadrado automático
    if cuadrado_automatico.left < 0:
        cuadrado_automatico.left = 0
    if cuadrado_automatico.right > ancho:
        cuadrado_automatico.right = ancho

    # Movimiento hacia arriba
    cuadrado_jugador.y -= velocidad_jugador
    cuadrado_automatico.y -= velocidad_automatico

    # Comprobar si el jugador o el automático han alcanzado la línea de meta
    if cuadrado_jugador.top >= linea_meta_y or cuadrado_automatico.top >= linea_meta_y:
        if cuadrado_jugador.top < linea_meta_y:
            ganador = "¡El jugador gana!"
            cuadrado_jugador.y = linea_meta_y
            cuadrado_automatico.y = linea_meta_y
        elif cuadrado_automatico.top <  linea_meta_y:
            ganador = "¡El cuadrado automático gana!"
            cuadrado_jugador.y = linea_meta_y
            cuadrado_automatico.y = linea_meta_y

        # Detener los cuadrados al final de la carrera
        

    # Llenar la pantalla con blanco
    screen.fill((255, 255, 255))

    # Dibujar los cuadrados
    pygame.draw.rect(screen, color_jugador, cuadrado_jugador)
    pygame.draw.rect(screen, color_automatico, cuadrado_automatico)

    # Dibujar la línea de meta
    pygame.draw.line(screen, color_meta, (0, linea_meta_y), (ancho, linea_meta_y), 5)

    # Mostrar el ganador
    if ganador:
        font = pygame.font.Font(None, 74)
        text = font.render(ganador, True, (0, 0, 0))
        text_rect = text.get_rect(center=(ancho // 2, alto // 2))
        screen.blit(text, text_rect)

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar el framerate
    clock.tick(30)
