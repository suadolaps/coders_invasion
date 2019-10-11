class GameStats:
    """Track statistics for coder invasion."""
    
    def __init__(self, ci_game):
        """Initialise statistics."""
        self.settings = ci_game.settings
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False
        
    def reset_stats(self):
        """Initialise statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
