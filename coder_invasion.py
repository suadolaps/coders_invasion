import pygame

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Inititalise pygame, settings and screen object.
    pygame.init()
    ci_settings = Settings()
    screen = pygame.display.set_mode(
        (ci_settings.screen_width, ci_settings.screen_height))
    pygame.display.set_caption("Coder Invasion")

    # Make a ship.
    ship = Ship(ci_settings, screen)

    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ci_settings, screen, ship)


run_game()
