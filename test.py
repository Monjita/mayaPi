import pygame
import sys

pygame.init()

# Crear ventana
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Test Pygame")

# Fuente y texto
font = pygame.font.Font(None, 36)
text = font.render("Pygame funcionando!", True, (255, 255, 255))

# Bucle principal
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    screen.blit(text, (50, 130))
    pygame.display.flip()

pygame.quit()
sys.exit()
