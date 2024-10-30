"""Initializing modules..."""
import pygame
from circleshape import CircleShape

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

    def draw(self, screen):
        """
        Draws the asteroid as a white circle on the provided screen.

        Args:
            screen (pygame.Surface): The screen surface where the asteroid is drawn.
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, delta_time):
        """
        Updates the asteroid's position based on its velocity and the delta time.

        Args:
            delta_time (float): The time interval since the last update, used to
                                adjust the position based on the velocity.
        """
        self.position += self.velocity * delta_time
