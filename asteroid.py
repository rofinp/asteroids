"""Initializing modules..."""

import pygame

import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    """
    Represents an Asteroid instance that inherits from the CircleShape class.

    Attributes:
        position (pygame.Vector2): The position of the asteroid on the screen.
        radius (float): The radius of the asteroid.
        velocity (pygame.Vector2): The velocity vector of the asteroid.
    """

    def __init__(self, x, y, radius):
        """
        Initializes an Asteroid object with the given position and radius.

        Args:
            x (float): The x-coordinate of the asteroid's initial position.
            y (float): The y-coordinate of the asteroid's initial position.
            radius (float): The radius of the asteroid.
        """
        super().__init__(x, y, radius)

    def split(self):
        """
        Splits the asteroid into two smaller asteroids, each moving in a different direction.
        The new asteroids are slightly faster and smaller than the original.
        """
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        velocity_one = self.velocity.rotate(random_angle)
        velocity_two = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Create two smaller asteroids at the current position
        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_one.velocity = velocity_one * 1.2
        asteroid_two.velocity = velocity_two * 1.2

    def draw(self, screen):
        """
        Draws the asteroid as a white circle on the provided screen.

        Args:
            screen (pygame.Surface): The screen surface where the asteroid is drawn.
        """
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, delta_time):
        """
        Updates the asteroid's position based on its velocity and the delta time.

        Args:
            delta_time (float): The time interval since the last update, used to
                                adjust the position based on the velocity.
        """
        self.position += self.velocity * delta_time
