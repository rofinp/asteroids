"""Initializes modules."""
import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    )

class Player(CircleShape):
    """Initializes a Player instance that inherits form CircleShape class"""
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def update(self, delta_time):
        """Updates the player's rotation based on key input."""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-delta_time)
        if keys[pygame.K_d]:
            self.rotate(delta_time)
        if keys[pygame.K_w]:
            self.move(delta_time)
        if keys[pygame.K_s]:
            self.move(-delta_time)

    def move(self, delta_time):
        """Moves the player based on key input."""
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * delta_time * PLAYER_TURN_SPEED

    def rotate(self, delta_time):
        """Rotates the player by changing the rotation angle based on input."""
        self.rotation += delta_time * PLAYER_TURN_SPEED

    def triangle(self):
        """
        A player will look like a triangle, 
        even though we'll use a circle to represent its hitbox
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Draws the white triangle player on the provided screen."""
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
