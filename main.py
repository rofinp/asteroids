"""Initializes modules."""

from asteroid import Asteroid
from asteroidfield import AsteroidField
from bullet import Bullet
from constants import (
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from player import Player


def main():
    import pygame

    print("Starting asteroids!")
    pygame.init()
    # Set GUI window screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # Groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    # Asteroids
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    AsteroidField()

    # Bullet
    Bullet.containers = (bullets, updateable, drawable)

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

        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print("Player collided with an asteroid!")
                print("Game over!")
                pygame.quit()
                return

        for asteroid in asteroids:
            for bullet in bullets:
                if asteroid.is_collision(bullet):
                    asteroid.split()
                    bullet.kill()

        screen.fill("black")

        for object in drawable:
            object.draw(screen)

        # Refresh the screen
        pygame.display.flip()

        # Limit the framerate to 60 FPS
        delta_time = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
