import pygame

pygame.init()

screen = pygame.display.set_mode((900, 900))
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        pygame.draw.rect(screen, (78, 215, 252), (0, 0, 200, 200))

        # syntax -> pygame.draw.rect(surface, color, rect(cords(left, top, width, height)), width=0)

    pygame.display.flip()