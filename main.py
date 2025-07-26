import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS
from player import Player
from asteroids import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()


def main():
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = (updateable,)
    Shot.containers = (shots, updateable, drawable)

    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, PLAYER_RADIUS)
    field = AsteroidField()

    running = True
    while running:
        fps = clock.tick(60)
        dt = fps / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updateable.update(dt)

        # Check for collisions between player and asteroids
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                pygame.quit()
                sys.exit()

        # Check for collisions between shots and asteroids
        for shot in shots:
            for asteroid in asteroids:
                if shot.collides_with(asteroid):
                    # When a bullet hits an asteroid, split the asteroid and remove the shot
                    shot.kill()
                    asteroid.split()

        screen.fill('black')
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    print('Starting Asteroids!')
    print('Screen width:', SCREEN_WIDTH)
    print('Screen height:', SCREEN_HEIGHT)
    main()
