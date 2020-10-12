class GameStats:
    """Track statistics for Alien Invasion Game"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        """reset stats for new game"""
        self.ship_left = self.settings.ship_limit