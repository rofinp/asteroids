"""Initializing modules..."""

import random

import pygame

from asteroid import Asteroid
from constants import (
    ASTEROID_KINDS,
    ASTEROID_MAX_RADIUS,
    ASTEROID_MAX_SPEED,
    ASTEROID_MIN_RADIUS,
    ASTEROID_MIN_SPEED,
    ASTEROID_SPAWN_RATE,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)


class AsteroidField(pygame.sprite.Sprite):
    """
    Represents a field of asteroids that spawn and move in random directions
    from the edges of the screen.

    Attributes:
        edges (list): Contains directional vectors and spawn positions for each
            edge of the screen.
        spawn_timer (float): Timer to control the interval at which asteroids spawn.
    """

    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + ASTEROID_MAX_RADIUS, y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, -ASTEROID_MAX_RADIUS),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + ASTEROID_MAX_RADIUS
            ),
        ],
    ]

    def __init__(self):
        """
        Initializes the AsteroidField instance, setting up the sprite group
        and the spawn timer.
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, radius, position, velocity):
        """
        Creates and initializes a new asteroid.

        Args:
            radius (float): Radius of the asteroid.
            position (pygame.Vector2): Starting position of the asteroid.
            velocity (pygame.Vector2): Initial velocity of the asteroid.
        """
        asteroid = Asteroid(position.x, position.y, radius)
        asteroid.velocity = velocity

    def update(self, delta_time):
        """
        Updates the asteroid field by checking if a new asteroid should spawn.
        If the spawn timer exceeds the spawn rate, a new asteroid is spawned
        at a random edge.

        Args:
            delta_time (float): Delta time since the last update.
        """
        self.spawn_timer += delta_time
        if self.spawn_timer > ASTEROID_SPAWN_RATE:
            self.spawn_timer = 0

            # spawn a new asteroid at a random edge
            edge = random.choice(self.edges)
            speed = random.randint(ASTEROID_MIN_SPEED, ASTEROID_MAX_SPEED)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            kind = random.randint(1, ASTEROID_KINDS)
            self.spawn(ASTEROID_MIN_RADIUS * kind, position, velocity)
