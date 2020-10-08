class Settings:
    """A class to store all settings for Alien Invasion"""
    # color
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    def __init__(self):
        """Initiate game's settings"""
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship settings
        self.ship_speed = 1.5 

        # bullet settings - dark grey 3x15 pixels
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # alien ship settings
        self.alien_speedx = 1
        self.alien_speedy = 10
        self.fleet_direction = 1
        self.alien_bg_color = self.BLACK
