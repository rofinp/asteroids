"""Initializes modules."""
import pygame
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
)

def main():
    """The Main Function"""
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Asteroids
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    asteroid_field = AsteroidField()

    # Players
    Player.containers = (updateable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    delta_time = 0

    while True:
        # This will check if the user has closed the window and exit the game loop if they do.
        # It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting asteroids!")
                pygame.quit()
                return

        for thing in updateable:
            thing.update(delta_time)

        for thing in asteroids:
            if thing.is_collision(player):
                print("Player collided with an asteroid!")
                print("Game over!")
                pygame.quit()
                return

        screen.fill("black")

        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()

        # Limit the framerate to 60 FPS
        delta_time = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
