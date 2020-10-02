import sys
import pygame
from settings import Settings

class AlienInvasion:
    """Class to manage game assets and behaviors"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()  # init Settings for screen
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        )  # set screen size
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (self.settings.bg_color) # set background color

    def run_game(self):
        """Start main loop of the game"""
        while True:
            # to listen to different events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.bg_color)
            # Fresh screen.  Make the most recently drawn screen visible
            pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()