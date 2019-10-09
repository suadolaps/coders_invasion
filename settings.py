class Settings():
    """A class to store all settings for Code Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1400
        self.screen_height = 800
        self.bg_color = (227, 232, 230)

        # Ship settings
        self.ship_speed_factor = 1.5
