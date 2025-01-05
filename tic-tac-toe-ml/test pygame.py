import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 600, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Board")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define board size and cell size
rows, cols = 10, 10
cell_size = width // cols

def draw_board():
    for row in range(rows):
        for col in range(cols):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(window, WHITE, rect)
            pygame.draw.rect(window, BLACK, rect, 1)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill(BLACK)
    draw_board()
    pygame.display.flip()

pygame.quit()
sys.exit()