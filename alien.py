import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ci_settings, screen):
        """Initialise the alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ci_settings = ci_settings

        # Lo
