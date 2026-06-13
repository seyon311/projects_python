import pygame


def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SPRITE_WIDTH, SPRITE_HEIGHT = 50, 50
    FPS = 60  # Higher FPS for smoother movement but faster sprite movement

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Move a Square")

    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'yellow': (255, 255, 0),
        'white': (255, 255, 255),
    }

    current_color = colors['white']

    x, y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

    clock = pygame.time.Clock()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        # Arrow key users

        if keys[pygame.K_LEFT]: x -= 5
        if keys[pygame.K_RIGHT]: x += 5
        if keys[pygame.K_UP]: y -= 5
        if keys[pygame.K_DOWN]: y += 5

        x = min(max(x, 0), SCREEN_WIDTH - SPRITE_WIDTH)     # This is the line that ensures the square stays within the screen boundaries horizontally
        y = min(max(y, 0), SCREEN_HEIGHT - SPRITE_HEIGHT)   # This is the line that ensures the square stays within the screen boundaries vertically

        if x == 0: current_color = colors['red']
        elif x == SCREEN_WIDTH - SPRITE_WIDTH: current_color = colors['green']
        elif y == 0: current_color = colors['blue']
        elif y == SCREEN_HEIGHT - SPRITE_HEIGHT: current_color = colors['yellow']
        else: current_color = colors['white']

        screen.fill((0, 0, 0))

        pygame.draw.rect(screen, current_color, (x, y, SPRITE_WIDTH, SPRITE_HEIGHT))
        pygame.display.flip()
        
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
