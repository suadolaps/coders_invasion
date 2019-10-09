import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Inititalise pygame, settings and screen object.
    pygame.init()
    ci_settings = Settings()
    screen = pygame.display.set_mode(
        (0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Coder Invasion")

    # Make a ship.
    ship = Ship(ci_settings, screen)
    # Make a group to store bullets in.
    bullets = Group()

    # Start the main loop for the game.
    while True:
        gf.check_events(ci_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_screen(ci_settings, screen, ship, bullets)


run_game()
