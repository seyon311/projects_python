import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN_NAME = "Bouncy Sprite Game"

SPRITE_COLOR_CHANGE_EVENT = pygame.USEREVENT + 1
BACKGROUND_COLOR_CHANGE_EVENT = pygame.USEREVENT + 2


# Background colors
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
DARK_BLUE = (0, 0, 139)


# Sprite colors
YELLOW = (179, 179, 0)
ROYAL_PURPLE = (138, 84, 153)
ORANGE = (255, 165, 0)
WHITE = (255, 255, 255)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.velocity = [random.choice([-1, 1]), random.choice([-1, 1])]

    def update(self):
        self.rect.move_ip(self.velocity)

        boundary_hit = False

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.velocity[0] = -self.velocity[0]
            boundary_hit = True    

        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.velocity[1] = -self.velocity[1]
            boundary_hit = True

        if boundary_hit:
            pygame.event.post(pygame.event.Event(SPRITE_COLOR_CHANGE_EVENT))
            pygame.event.post(pygame.event.Event(BACKGROUND_COLOR_CHANGE_EVENT))

    def change_color(self):
        self.image.fill(random.choice([YELLOW, ROYAL_PURPLE, ORANGE, WHITE]))

def change_background_color():
    global bg_color
    bg_color = random.choice([BLUE, LIGHT_BLUE, DARK_BLUE])

all_sprites_list = pygame.sprite.Group()

sp1 = Sprite(YELLOW, 50, 50)

sp1.rect.x = random.randint(0, SCREEN_WIDTH - sp1.rect.width)
sp1.rect.y = random.randint(0, SCREEN_HEIGHT - sp1.rect.height)

all_sprites_list.add(sp1)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_NAME)

bg_color = BLUE

screen.fill(bg_color)

running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == SPRITE_COLOR_CHANGE_EVENT:
            sp1.change_color()
        elif event.type == BACKGROUND_COLOR_CHANGE_EVENT:
            change_background_color()

    all_sprites_list.update()    
    screen.fill(bg_color)
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(240) # 240 fps

pygame.quit()