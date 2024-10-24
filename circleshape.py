"""Initializes pygame module."""
import pygame

class CircleShape(pygame.sprite.Sprite):
    """Initializes a CircleShape instance."""
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """Draws the circle on the provided screen."""
        pass

    def update(self, delta_time):
        """Updates the position and velocity of the circle based on the time delta."""
        pass