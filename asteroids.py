import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        for g in self.containers:
            g.add(self)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            "white",
            (int(self.position.x), int(self.position.y)),
            int(self.radius),
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt
