import pygame

pygame.init()

Width, Height = 400, 500
Caption = "Background"

screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption(Caption)

background_image = pygame.transform.scale(pygame.image.load("cool.png").convert(), (Width, Height))

ship = pygame.transform.scale(pygame.image.load("Myship.png").convert_alpha(), (100, 100))
ship_rect = ship.get_rect(center=(Width // 2, Height // 2 - 30))

text = pygame.font.Font(None, 36).render("This is a background image", True, (255, 255, 255))
text_rect = text.get_rect(center=(Width // 2, Height - 50))

def game_loop():
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.blit(background_image, (0, 0))
        screen.blit(ship, ship_rect)
        screen.blit(text, text_rect)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()    


if __name__ == "__main__":
    game_loop()
    



