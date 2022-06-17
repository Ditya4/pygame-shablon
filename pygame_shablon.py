import pygame


def main():
    run = True
    clock = pygame.time.Clock()
    pygame.init()
    surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Cannon")
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        surface.fill((0, 0, 0))
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    WINDOW_WIDTH = 600
    WINDOW_HEIGHT = 650
    main()
