import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
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
            2
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        # Always kill this asteroid
        self.kill()

        # If this is a small asteroid, just return
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Calculate new radius for child asteroids
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Generate random angle for splitting
        random_angle = random.uniform(20, 50)

        # Create two new velocity vectors by rotating the current velocity
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)

        # Scale up velocities to make child asteroids faster
        velocity1 *= 1.2
        velocity2 *= 1.2

        # Create two new smaller asteroids
        position_x = self.position.x
        position_y = self.position.y

        asteroid1 = Asteroid(position_x, position_y, new_radius)
        asteroid1.velocity = velocity1

        asteroid2 = Asteroid(position_x, position_y, new_radius)
        asteroid2.velocity = velocity2
