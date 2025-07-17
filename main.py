import pygame
from constants import *

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    while True:
        screen.fill('black')
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    print('Starting Asteroids!')
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)

if __name__ == "__main__":
    main()
