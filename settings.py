class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initiate game's settings"""
        # screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5  # move by 1.5 pixel instead 1