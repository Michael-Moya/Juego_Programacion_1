import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Usando get_ticks() en lugar de delay")

# Crear un reloj para controlar los fotogramas por segundo
clock = pygame.time.Clock()

# Variables de tiempo
start_time = pygame.time.get_ticks()
wait_time = 200  # Tiempo de espera en milisegundos
elapsed_time = 0

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calcular el tiempo transcurrido
    current_time = pygame.time.get_ticks()
    elapsed_time = current_time - start_time
    print(elapsed_time)

    # Verificar si ha pasado el tiempo de espera
    if elapsed_time >= wait_time:
        print("Han pasado 100 milisegundos.")
        # Reiniciar el temporizador
        start_time = current_time

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Mostrar el tiempo transcurrido
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f'Tiempo transcurrido: {elapsed_time // 1000} segundos', True, (255, 255, 255))
    screen.blit(text_surface, (50, 50))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar los FPS
    clock.tick(60)
