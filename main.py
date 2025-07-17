import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
dt = 0.0

def main():
    while True:
        screen.fill('black')
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fps = clock.tick(60)
                dt = fps / 1000.0
                return
    print('Starting Asteroids!')
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
