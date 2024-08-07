import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Círculos que caen")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Variables del juego
circles = []
circle_radius = 20
circle_speed = 5
square_size = 50
square_pos = [WIDTH // 2, HEIGHT - 100]
lives = 3
game_paused = False

# Función para crear círculos
def create_circle():
    x_pos = random.randint(0 + circle_radius, WIDTH - circle_radius)
    y_pos = 0  # Comienza desde la parte superior
    circles.append([x_pos, y_pos])

# Función para mover círculos
def move_circles():
    for circle in circles:
        circle[1] += circle_speed  # Mover hacia abajo

# Función para comprobar colisiones
def check_collision(square_pos):
    global circles, lives
    for circle in circles:
        if (circle[0] - square_pos[0]) ** 2 + (circle[1] - square_pos[1]) ** 2 < (circle_radius + square_size / 2) ** 2:
            circles.remove(circle)  # Eliminar el círculo si hay colisión
            lives -= 1  # Perder una vida
            if lives <= 0:
                return True  # Indicar que el juego debe pausar
    return False  # Indicar que el juego puede continuar

# Bucle principal del juego
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_paused:
        # Crear nuevos círculos
        if random.randint(1, 20) == 1:  # Ajustar la frecuencia de generación
            create_circle()

        # Mover círculos
        move_circles()
        
        # Comprobar colisiones
        if check_collision(square_pos):
            game_paused = True  # Pausar el juego si no hay vidas

        # Controlar el cuadrado
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and square_pos[0] > 0:
            square_pos[0] -= 5
        if keys[pygame.K_RIGHT] and square_pos[0] < WIDTH - square_size:
            square_pos[0] += 5

    # Dibujar todo
    screen.fill(WHITE)
    for circle in circles:
        pygame.draw.circle(screen, RED, (circle[0], circle[1]), circle_radius)
    pygame.draw.rect(screen, BLUE, (square_pos[0], square_pos[1], square_size, square_size))

    # Mostrar el número de vidas
    font = pygame.font.Font(None, 36)
    text = font.render(f'Vidas: {lives}', True, BLACK)
    screen.blit(text, (10, 10))

    # Mostrar pausa si el juego está pausado
    if game_paused:
        pause_text = font.render('¡Juego Pausado! Presiona R para reiniciar', True, BLACK)
        screen.blit(pause_text, (WIDTH // 2 - pause_text.get_width() // 2, HEIGHT // 2))

        # Comprobar si se presiona R para reiniciar
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            lives = 3
            circles.clear()
            square_pos = [WIDTH // 2, HEIGHT - 100]
            game_paused = False

    pygame.display.flip()
    clock.tick(30)  # Limitar a 30 FPS
