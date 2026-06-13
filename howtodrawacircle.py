import pygame

pygame.init()

window = pygame.display.set_mode((500, 500))
window.fill((168, 217, 255))

BLUE = (31, 157, 255)

pygame.draw.circle(window, BLUE, (250, 250), 100)
# syntax -> pygame.draw.circle(surface, color, center, radius, width=0)

pygame.draw.circle(window, BLUE, (400, 400), 50, 3)

pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()                