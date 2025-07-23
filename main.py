import pygame
from constants import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def main():

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y, PLAYER_RADIUS)
    running = True
    while running:
        fps = clock.tick(60)
        dt = fps / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.update(dt)

        screen.fill('black')
        player.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    print('Starting Asteroids!')
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)
    main()
