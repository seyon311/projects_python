import pygame

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_COLOR = (255, 255, 255)

SPRITE_WIDTH, SPRITE_HEIGHT = 50, 50

# Player 1 (WASD)
p1_x, p1_y = 200, 300
p1_color = (52, 183, 235)

# Player 2 (Arrow Keys)
p2_x, p2_y = 600, 300
p2_color = (235, 52, 52)

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Two Squares")

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player 1 movement (WASD)
    if keys[pygame.K_a]: p1_x -= 5
    if keys[pygame.K_d]: p1_x += 5
    if keys[pygame.K_w]: p1_y -= 5
    if keys[pygame.K_s]: p1_y += 5

    # Player 2 movement (Arrow Keys)
    if keys[pygame.K_LEFT]: p2_x -= 5
    if keys[pygame.K_RIGHT]: p2_x += 5
    if keys[pygame.K_UP]: p2_y -= 5
    if keys[pygame.K_DOWN]: p2_y += 5

    # Keep players inside screen
    p1_x = min(max(p1_x, 0), SCREEN_WIDTH - SPRITE_WIDTH)
    p1_y = min(max(p1_y, 0), SCREEN_HEIGHT - SPRITE_HEIGHT)

    p2_x = min(max(p2_x, 0), SCREEN_WIDTH - SPRITE_WIDTH)
    p2_y = min(max(p2_y, 0), SCREEN_HEIGHT - SPRITE_HEIGHT)

    window.fill(SCREEN_COLOR)

    # Draw both players
    pygame.draw.rect(window, p1_color, (p1_x, p1_y, SPRITE_WIDTH, SPRITE_HEIGHT))
    pygame.draw.rect(window, p2_color, (p2_x, p2_y, SPRITE_WIDTH, SPRITE_HEIGHT))

    pygame.display.flip()

pygame.quit()

