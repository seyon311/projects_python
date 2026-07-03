import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_COLOR = (255, 255, 255)
SCREEN_NAME = "Sprite Movement"

P_X, P_Y = 400, 300
P_COLOR = (52, 52, 235)

ENEMIES_MAX_X, ENEMIES_MIN_X = 700, 100
ENEMIES_MAX_Y, ENEMIES_MIN_Y = 500, 100
ENEMIES_COLOR = (235, 52, 52)

NUM_OF_ENEMIES = 7

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_NAME)

px, py = P_X, P_Y
px_delta, py_delta = 0, 0

enemy_x = []
enemy_y = []

for _i in range(NUM_OF_ENEMIES):
    enemy_x.append(random.randint(ENEMIES_MIN_X, ENEMIES_MAX_X))
    enemy_y.append(random.randint(ENEMIES_MIN_Y, ENEMIES_MAX_Y))

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color, height, width):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center = (x, y))

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 5
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_d] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += 5

PLAYER = Sprite(px, py, P_COLOR, 50, 50)

ENEMIES = pygame.sprite.Group()

for i in range(NUM_OF_ENEMIES):
    while True:
        x = random.randint(ENEMIES_MIN_X, ENEMIES_MAX_X)
        y = random.randint(ENEMIES_MIN_Y, ENEMIES_MAX_Y)

        new_enemy = Sprite(x, y, ENEMIES_COLOR, 50, 50)

        # Check collision with existing enemies
        if not pygame.sprite.spritecollideany(new_enemy, ENEMIES):
            ENEMIES.add(new_enemy)
            break

running = True
clock = pygame.time.Clock()
score = 0
start_time = pygame.time.get_ticks()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    PLAYER.update()

    hit_enemy = pygame.sprite.spritecollideany(PLAYER, ENEMIES)
    if hit_enemy:
        ENEMIES.remove(hit_enemy)
        score += 1
        print("Score:", score)

        # Close window when all enemies are gone
        if score == NUM_OF_ENEMIES:
            
            running = False

            end_time = pygame.time.get_ticks()
            time_elasped = (end_time - start_time) / 1000

            print("All enemies eliminated!")
            print("It took you", time_elasped, "seconds to eliminate all enemies.")

    screen.fill(SCREEN_COLOR)
    screen.blit(PLAYER.image, PLAYER.rect)

    ENEMIES.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()    