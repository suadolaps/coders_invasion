import sys
import pygame
from settings import Settings
from ship import Ship


def run_game():
    # Inititalise pygame, settings and screen object.
    pygame.init()
    ci_settings = Settings()
    screen = pygame.display.set_mode(
        (ci_settings.screen_width, ci_settings.screen_height))
    pygame.display.set_caption("Coder Invasion")

    # Make a ship.
    ship = Ship(screen)

    # Start the main loop for the game.
    while True:

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Redraw the screen during each pass through the loop.
        screen.fill(ci_settings.bg_color)
        ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
