"""Initializes modules."""
import pygame
from player import Player
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS,
)

def main():
    """The Main Function"""
    print("Starting asteroids!")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    delta_time = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        # This will check if the user has closed the window and exit the game loop if they do.
        # It will make the window's close button work.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting asteroids!")
                pygame.quit()
                return
        player.update(delta_time)
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
