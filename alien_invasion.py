import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """Class to manage game assets and behaviors"""

    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        # set screen using settings.py
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.bg_color = (self.settings.bg_color) # set background color

        # initiate ship.  Needs to pass Alien Invasion class (self)
        self.ship = Ship(self)


    def run_game(self):
        """Start main loop of the game"""
        while True:
            # to listen to keystroke events
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """private fn for AlienInvasion Class:  checks key events"""
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # if a key is pressed down
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Actions responding to key down"""
        if event.key == pygame.K_RIGHT :
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT :
            self.ship.moving_left = True
        if event.key == pygame.K_q:  # if user presses q/Q then quit
            sys.exit()

    def _check_keyup_events(self, event):
        """Actions responding to key up"""
        if event.key == pygame.K_RIGHT :
            self.ship.moving_left = False
        if event.key == pygame.K_LEFT :
            self.ship.moving_right = False

    def _update_screen(self):
        """private fn:  update screen"""
        # erase screen by filling it with bg_color
        self.screen.fill(self.bg_color)
        # draw image onto screen
        self.ship.blitme()
        # Fresh screen.  Make the most recently drawn screen visible
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()