import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("primitiva con animacion")
# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PINK = (255, 182, 193)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
GREEN = (0, 255, 0)
DARK_GRAY = (50, 50, 50)

# circulo
def dibujar_circulo(x, y, radio, color):
    pygame.draw.circle(screen, color, (int(x), int(y)), radio)

# rectangulo
def dibujar_rectangulo(x, y, ancho, alto, color):
    pygame.draw.rect(screen, color, (int(x), int(y), ancho, alto))

# triangulo
def dibujar_triangulo(x, y, base, altura, color):
    puntos = [(x, y), (x + base, y), (x + base / 2, y - altura)]
    pygame.draw.polygon(screen, color, puntos)

# Posiciones iniciales
hombro_x, hombro_y = WIDTH // 2 + 60, HEIGHT // 2 - 80
brazo_ancho, brazo_alto = 60, 55
angulo = 0

clock = pygame.time.Clock()
running = True
frame = 0

while running:
    screen.fill(DARK_GRAY)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # cabeza
    dibujar_circulo(WIDTH // 2, HEIGHT // 2 - 120, 60, PINK)
    pygame.draw.line(screen, BLACK, (320, 300), (270, 300), 2)
    # ojos
    dibujar_circulo(WIDTH // 2 - 20, HEIGHT // 2 - 140, 10, WHITE)  
    dibujar_circulo(WIDTH // 2 + 20, HEIGHT // 2 - 140, 10, WHITE)  
    
    # pupilas
    desplazamiento_ojos = math.sin(frame * 0.1) * 5
    dibujar_circulo(WIDTH // 2 - 20 + desplazamiento_ojos, HEIGHT // 2 - 140, 5, BLUE)
    dibujar_circulo(WIDTH // 2 + 20 + desplazamiento_ojos, HEIGHT // 2 - 140, 5, BLUE)

    # torso
    dibujar_rectangulo(WIDTH // 2 - 40, HEIGHT // 2 - 60, 80, 120, BLUE)

    # brazo izquierdo
    dibujar_rectangulo(WIDTH // 2 - 100, HEIGHT // 2 - 40, brazo_ancho, brazo_alto, PINK)

    # brazo derecho
    angulo = math.sin(frame * 0.1) * math.pi / 4
    brazo_x = hombro_x + math.cos(angulo) * 60
    brazo_y = hombro_y + math.sin(angulo) * 30
    dibujar_rectangulo(brazo_x, brazo_y, brazo_ancho, brazo_alto, PINK)

    # piernas
    dibujar_rectangulo(WIDTH // 2 - 39, HEIGHT // 2 + 60, 40, 80, ORANGE)  
    dibujar_rectangulo(WIDTH // 2 + 1, HEIGHT // 2 + 60, 40, 80, ORANGE)  

    # Sombrero
    offset_sombrero = math.sin(frame * 0.1) * 5
    dibujar_triangulo(WIDTH // 2 - 55, HEIGHT // 2 - 190 + offset_sombrero, 120, 80, GREEN)

    pygame.display.flip()
    frame += 1
    clock.tick(60)

pygame.quit()
sys.exit()
