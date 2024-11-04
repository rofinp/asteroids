"""Initializing modules..."""

import pygame


class CircleShape(pygame.sprite.Sprite):
    """
    Represents a circular shape in the game, inheriting from pygame's Sprite class.

    Attributes:
        position (pygame.Vector2): The current position of the circle.
        velocity (pygame.Vector2): The current velocity of the circle.
        radius (float): The radius of the circle.
    """

    def __init__(self, x, y, radius):
        """
        Initializes a CircleShape object with a specified position and radius.

        Args:
            x (float): The x-coordinate of the circle's initial position.
            y (float): The y-coordinate of the circle's initial position.
            radius (float): The radius of the circle.
        """
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """
        Draws the circle on the provided screen.

        Args:
            screen (pygame.Surface): The surface on which the circle is drawn.
        """
        pass

    def update(self, delta_time):
        """
        Updates the circle's position based on its velocity and the elapsed time.

        Args:
            delta_time (float): The time delta since the last update, used to scale movement.
        """
        pass

    def is_collision(self, object):
        """
        Checks if the circle intersects with another object.

        Args:
            object (CircleShape): The other object to check for intersection.

        Returns:
            bool: True if the circle intersects with the other object, False otherwise.
        """
        distance = self.position.distance_to(object.position)
        return distance <= self.radius + object.radius
