import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    containers = ()
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        for g in self.containers:
            g.add(self)

    def draw(self, screen):
        position = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(
            screen,
            "white",
            position,
            int(self.radius),
            0  # Filled circle for the shot
        )

    def update(self, dt):
        self.position += self.velocity * dt
