import os
import pygame
import time
import datetime

# Forzar salida por framebuffer /dev/fb1 (pantalla SPI)
os.putenv('SDL_FBDEV', '/dev/fb1')

# Inicializar Pygame sin X11
pygame.display.init()
pygame.font.init()

# Resolución de tu pantalla SPI
WIDTH, HEIGHT = 480, 320
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.mouse.set_visible(False)

# Paleta colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Cargar imágenes PNG
try:
    imagen_cero = pygame.image.load("cero_v2.png")
    imagen_cinco = pygame.image.load("cinco.png")
except pygame.error as e:
    print(f"Error cargando imágenes: {e}")
    imagen_cero = None
    imagen_cinco = None


def draw_digit(digit_matrix, x, y, size=12, color=WHITE):
    """Dibuja un número basado en una matriz pixel art.
    
    Soporta dos tipos de matrices:
    - DIGITS: Matrices pequeñas (7 filas, 5 columnas)
    - DIGITSMAYA: Matrices grandes (más filas, más columnas)
    """
    for row_index, row in enumerate(digit_matrix):
        for col_index, pixel in enumerate(row):
            if pixel == "1":
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(
                        x + col_index * size,
                        y + row_index * size,
                        size - 2 if size > 1 else size,
                        size - 2 if size > 1 else size,
                    )
                )

def scale_image_to_fit(image, max_width, max_height):
    """Escala una imagen para que quepa dentro de un área manteniendo aspecto."""
    if image is None:
        return None
    
    img_width, img_height = image.get_size()
    
    # Calcular escala manteniendo aspecto
    scale_x = max_width / img_width
    scale_y = max_height / img_height
    scale = min(scale_x, scale_y)
    
    new_width = int(img_width * scale)
    new_height = int(img_height * scale)
    
    return pygame.transform.scale(image, (new_width, new_height))

def draw_time():
    """Dibuja cero.png en la primera mitad de la pantalla."""
    half_width = WIDTH // 2
    margin_x = 20
    
    # Centro de la mitad izquierda
    center_x = half_width // 2
    center_y = HEIGHT // 2
    
    # Escalar imagen para que quepa en la mitad
    available_width = half_width - 2 * margin_x
    available_height = HEIGHT - 2 * margin_x
    
    scaled_img = scale_image_to_fit(imagen_cero, available_width, available_height)
    
    if scaled_img:
        img_rect = scaled_img.get_rect(center=(center_x, center_y))
        screen.blit(scaled_img, img_rect)

def draw_second_image():
    """Dibuja cinco.png en la segunda mitad de la pantalla."""
    half_width = WIDTH // 2
    margin_x = 20
    
    # Centro de la mitad derecha
    center_x = half_width + half_width // 2
    center_y = HEIGHT // 2
    
    # Escalar imagen para que quepa en la mitad
    available_width = half_width - 2 * margin_x
    available_height = HEIGHT - 2 * margin_x
    
    scaled_img = scale_image_to_fit(imagen_cinco, available_width, available_height)
    
    if scaled_img:
        img_rect = scaled_img.get_rect(center=(center_x, center_y))
        screen.blit(scaled_img, img_rect)

def draw_second_dot():
    """Dibuja un punto que parpadea según los segundos (segundero)."""
    current_second = datetime.datetime.now().second
    
    # Parpadea cada segundo (alternando entre visible y no visible)
    if current_second % 2 == 0:  # Par = visible, Impar = invisible
        dot_size = 8
        dot_x = WIDTH - 15
        dot_y = 10
        pygame.draw.rect(screen, RED, pygame.Rect(dot_x, dot_y, dot_size, dot_size))

def main():
    while True:
        screen.fill(BLACK)
        draw_time()
        draw_second_image()
        draw_second_dot()
        pygame.display.update()
        time.sleep(0.1)  # Mayor frecuencia para mejor precisión del parpadeo

if __name__ == "__main__":
    main()
