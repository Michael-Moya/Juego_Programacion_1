import pygame
import threading
import time

# Inicializa Pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mensaje con Hilos")

# Colores
black = (0, 0, 0)
white = (255, 255, 255)

# Fuente
font = pygame.font.Font(None, 74)

# Variable para el mensaje
message = ""
message_displayed = False

def display_message_after_delay(delay):
    global message, message_displayed
    time.sleep(delay)
    message = "¡Hola, Pygame!"
    message_displayed = True

# Inicia el hilo para mostrar el mensaje después de 5 segundos
thread = threading.Thread(target=display_message_after_delay, args=(5,))
thread.start()

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Rellena la pantalla de negro
    screen.fill(black)

    # Si el mensaje debe ser mostrado, dibújalo en la pantalla
    if message_displayed:
        text = font.render(message, True, white)
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)

    # Actualiza la pantalla
    pygame.display.flip()

# Cierra Pygame
pygame.quit()
