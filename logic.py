import pygame

pygame.init()

screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Drawing")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Black background
    pygame.draw.circle(screen, (255, 0, 0), (300, 200), 50)  # Red circle

    pygame.display.flip()

pygame.quit()