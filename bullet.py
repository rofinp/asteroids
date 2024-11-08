"""Initializing modules..."""

import pygame
from circleshape import CircleShape
from constants import BULLET_RADIUS


class Bullet(CircleShape):
    """
    Represents a Bullet instance that inherits from the CircleShape class.

    Attributes:
      position (pygame.Vector2): The position of the bullet on the screen.
      radius (float): The radius of the bullet.
      velocity (pygame.Vector2): The velocity vector of the bullet.
    """

    def __init__(self, x, y):
        """
        Initializes a Bullet object with the given position and radius.

        Args:
          x (float): The x-coordinate of the bullet's initial position.
          y (float): The y-coordinate of the bullet's initial position.
        """
        super().__init__(x, y, BULLET_RADIUS)

    def draw(self, screen):
        """
        Draws the bullet as a red circle on the provided screen.

        Args:
          screen (pygame.Surface): The screen surface where the bullet is drawn.
        """
        pygame.draw.circle(screen, "yellow", self.position, self.radius, 2)

    def update(self, delta_time):
        """
        Updates the bullet's position based on its velocity and the delta time.

        Args:
          delta_time (float): The time interval since the last update, used to adjust
                              the position based on the velocity.
        """
        self.position += self.velocity * delta_time
