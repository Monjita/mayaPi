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

# Paleta colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Matrices de números pixel art 5x7
DIGITSMAYA = {
    "0": [
    "...111111111111111111111...",
    "..1...1......1......1...1..",
    ".1...1......1......1.....1.",
    "1....1......1......1......1",
    "1....1......1......1......1",
    "11...1......1......1.....11",
    "1.1...1......1......1...1.1",
    "1..111111111111111111111..1",
    "1.........................1",
    "1.........................1",
    ".1.......................1.",
    "..1.....................1..",
    "...111111111111111111111...",
    ],
    "1": [
    "....1....",
    "..11111..",
    ".1111111.",
    ".1111111.",
    "111111111",
    ".1111111.",
    ".1111111.",
    "..11111..",
    "....1...."
]

}


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

def draw_time():
    """Dibuja el 0 de DIGITSMAYA en la primera mitad de la pantalla."""
    half_width = WIDTH // 2
    margin_x = 20
    
    # Centro de la mitad izquierda
    center_x = half_width // 2
    center_y = HEIGHT // 2
    
    # Dibujar el 0 de DIGITSMAYA
    digit_matrix = DIGITSMAYA["0"]
    
    # Calcular tamaño de píxel para que quepa en la mitad con márgenes
    available_width = half_width - 2 * margin_x
    available_height = HEIGHT - 2 * margin_x
    
    # Dimensiones del dígito
    digit_width = len(digit_matrix[0])  # 23 píxeles
    digit_height = len(digit_matrix)    # 13 píxeles
    
    # Calcular tamaño del píxel
    pixel_size_x = available_width / digit_width * 0.8
    pixel_size_y = available_height / digit_height * 0.8
    pixel_size = min(pixel_size_x, pixel_size_y)
    
    # Calcular posición para centrar
    total_width = digit_width * pixel_size
    total_height = digit_height * pixel_size
    
    x_pos = center_x - total_width // 2
    y_pos = center_y - total_height // 2
    
    # Dibujar el dígito
    draw_digit(digit_matrix, int(x_pos), int(y_pos), size=int(pixel_size), color=RED)

def draw_second_image():
    """Dibuja el 1 de DIGITSMAYA en la segunda mitad de la pantalla."""
    half_width = WIDTH // 2
    margin_x = 20
    
    # Centro de la mitad derecha
    center_x = half_width + half_width // 2
    center_y = HEIGHT // 2
    
    # Dibujar el 1 de DIGITSMAYA
    digit_matrix = DIGITSMAYA["1"]
    
    # Calcular tamaño de píxel para que quepa en la mitad con márgenes
    available_width = half_width - 2 * margin_x
    available_height = HEIGHT - 2 * margin_x
    
    # Dimensiones del dígito
    digit_width = len(digit_matrix[0])  # 10 píxeles
    digit_height = len(digit_matrix)    # 9 píxeles
    
    # Calcular tamaño del píxel
    pixel_size_x = available_width / digit_width * 0.8
    pixel_size_y = available_height / digit_height * 0.8
    pixel_size = min(pixel_size_x, pixel_size_y)
    
    # Calcular posición para centrar
    total_width = digit_width * pixel_size
    total_height = digit_height * pixel_size
    
    x_pos = center_x - total_width // 2
    y_pos = center_y - total_height // 2
    
    # Dibujar el dígito
    draw_digit(digit_matrix, int(x_pos), int(y_pos), size=int(pixel_size), color=RED)

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
