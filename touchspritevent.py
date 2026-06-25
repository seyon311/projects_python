import pygame

pygame.init()

fps = 120

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_COLOR = (255, 255, 255)
SCREEN_NAME = "Custom Event"

sp1x, sp1y = 600, 300
sp1_color = (235, 52, 52)
sp1W, sp1H = 50, 50

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_NAME)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color, height, width):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x, y))

    def update(self):
        # (WASD)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_s]:
            self.rect.y += 5
        if keys[pygame.K_a]:
            self.rect.x -= 5
        if keys[pygame.K_d]:
            self.rect.x += 5

player = Sprite(sp1x, sp1y, sp1_color, sp1W, sp1H)
all_sprites = pygame.sprite.Group(player)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Check if touching border
    touching_border = (
        player.rect.left <= 0 or
        player.rect.right >= SCREEN_WIDTH or
        player.rect.top <= 0 or
        player.rect.bottom >= SCREEN_HEIGHT
)
     # Change screen colour
    if touching_border:
        SCREEN_COLOR = (0, 0, 0)
    else:
        SCREEN_COLOR = (255, 255, 255)

    window.fill(SCREEN_COLOR)
    all_sprites.draw(window)

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
