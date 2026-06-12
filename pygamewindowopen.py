import pygame

pygame.init()

window = pygame.display.set_mode((400, 500))

open = True

while open:
    for event in pygame.event.get():
        if event .type == pygame.QUIT:
            open = False

pygame.quit()
