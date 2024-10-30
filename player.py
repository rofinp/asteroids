"""Initializing modules..."""
import pygame
from circleshape import CircleShape
from constants import (
    PLAYER_RADIUS,
    PLAYER_TURN_SPEED,
    )

class Player(CircleShape):
    """
    Represents a Player instance that inherits from the CircleShape class.

    Attributes:
        position (pygame.Vector2): The current position of the player on the screen.
        rotation (float): The current rotation angle of the player in degrees.
        radius (float): The radius of the player's hitbox.
    """
    def __init__(self, x, y):
        """
        Initializes a Player object with a specified position and default radius.

        Args:
            x (float): The x-coordinate of the player's initial position.
            y (float): The y-coordinate of the player's initial position.
        """
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    def update(self, delta_time):
        """
        Updates the player's rotation and position based on keyboard input.

        Args:
            delta_time (float): The time elapsed since the last update, 
                                used for movement and rotation speed.
        """
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
        """
        Moves the player forward or backward based on rotation and input.

        Args:
            delta_time (float): The time elapsed since the last update,
                                used to scale the movement speed.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * delta_time * PLAYER_TURN_SPEED

    def rotate(self, delta_time):
        """
        Rotates the player by adjusting the rotation angle.

        Args:
            delta_time (float): The time elapsed since the last update,
                                used to scale the rotation speed.
        """
        self.rotation += delta_time * PLAYER_TURN_SPEED

    def triangle(self):
        """
        Calculates the vertices of a triangle to represent the player visually.

        Returns:
            list[pygame.Vector2]: A list of three points forming a triangle 
                                  shape for the player.
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """
        Draws the player's triangle shape on the provided screen.

        Args:
            screen (pygame.Surface): The screen surface where the player is drawn.
        """
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
