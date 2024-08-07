import pygame
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Temporizador con set_timer")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Variables del temporizador
timer_event = pygame.USEREVENT + 1  # Crear un nuevo evento
pygame.time.set_timer(timer_event, 1000)  # Evento cada 1000 ms (1 segundo)

# Contador
counter = 0

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == timer_event:
            
            counter += 1  # Incrementar el contador cada segundo
            print(counter)

    # Limpiar la pantalla
    screen.fill(BLACK)

    # Mostrar el contador
    font = pygame.font.Font(None, 74)
    text = font.render(f'Tiempo: {counter}s', True, WHITE)
    screen.blit(text, (250, 250))

    # Actualizar la pantalla
    pygame.display.flip()

    # Controlar la velocidad del bucle
    pygame.time.Clock().tick(60)  # Limitar a 60 FPS

# Salir de Pygame
pygame.quit()
