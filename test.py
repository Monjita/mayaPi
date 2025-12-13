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

# Paleta simple (puedes hacer tus colores mayas)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Matrices de números pixel art 5x7 (puedes cambiar por números mayas)
DIGITS = {
    "0": [
        "11111",
        "1...1",
        "1..11",
        "1.1.1",
        "11..1",
        "1...1",
        "11111"
    ],
    "1": [
        "..1..",
        ".11..",
        "..1..",
        "..1..",
        "..1..",
        "..1..",
        "11111"
    ],
    "2": [
        "11111",
        "....1",
        "....1",
        "11111",
        "1....",
        "1....",
        "11111"
    ],
    "3": [
        "11111",
        "....1",
        "....1",
        "11111",
        "....1",
        "....1",
        "11111"
    ],
    "4": [
        "1...1",
        "1...1",
        "1...1",
        "11111",
        "....1",
        "....1",
        "....1"
    ],
    "5": [
        "11111",
        "1....",
        "1....",
        "11111",
        "....1",
        "....1",
        "11111"
    ],
    "6": [
        "11111",
        "1....",
        "1....",
        "11111",
        "1...1",
        "1...1",
        "11111"
    ],
    "7": [
        "11111",
        "....1",
        "...1.",
        "..1..",
        ".1...",
        ".1...",
        ".1..."
    ],
    "8": [
        "11111",
        "1...1",
        "1...1",
        "11111",
        "1...1",
        "1...1",
        "11111"
    ],
    "9": [
        "11111",
        "1...1",
        "1...1",
        "11111",
        "....1",
        "....1",
        "11111"
    ],
    ":": [
        "..",
        "..",
        "1.",
        "..",
        "1.",
        "..",
        ".."
    ]
}

def draw_digit(digit_matrix, x, y, size=12, color=WHITE):
    """Dibuja un número basado en una matriz pixel art."""
    for row_index, row in enumerate(digit_matrix):
        for col_index, pixel in enumerate(row):
            if pixel == "1":
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(
                        x + col_index * size,
                        y + row_index * size,
                        size - 2,
                        size - 2,
                    )
                )

def draw_time():
    now = datetime.datetime.now().strftime("%H:%M")
    # Centrar el reloj horizontalmente (ancho aproximado de HH:MM es 340px)
    x = (WIDTH - 340) // 2

    for char in now:
        if char == ":":
            draw_digit(DIGITS[":"], x, 100, size=12, color=WHITE)
            x += 20
        else:
            draw_digit(DIGITS[char], x, 100, size=12, color=WHITE)
            x += 80  # Espaciado entre dígitos

def draw_second_dot():
    """Dibuja un punto que parpadea según los segundos (segundero)."""
    current_second = datetime.datetime.now().second
    
    # Parpadea cada segundo (alternando entre visible y no visible)
    if current_second % 2 == 0:  # Par = visible, Impar = invisible
        dot_size = 8
        dot_x = WIDTH - 15
        dot_y = 10
        pygame.draw.rect(screen, WHITE, pygame.Rect(dot_x, dot_y, dot_size, dot_size))

def main():
    while True:
        screen.fill(BLACK)
        draw_time()
        draw_second_dot()
        pygame.display.update()
        time.sleep(0.1)  # Mayor frecuencia para mejor precisión del parpadeo

if __name__ == "__main__":
    main()
