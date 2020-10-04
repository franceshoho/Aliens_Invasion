import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

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

        # initiate ship.  need to pass in self as ai_game
        self.ship = Ship(self)
        # create a group of bullets.
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start main loop of the game"""
        while True:
            # to listen to keystroke events
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

    def _update_bullets(self):
        """update position of bullets and remove bullets when they
        pass top of screen"""
        self.bullets.update()
        self._remove_bullets()

    def _remove_bullets(self):
        # remove bullets after they disappear from screen
        # use a copy because we can't remove item within a loop
        for bullet in self.bullets.copy() :
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)

    def _check_events(self):
        """private fn for AlienInvasion Class:  checks key events"""
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                sys.exit()
            elif event.type == pygame.KEYDOWN:
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
        if event.key == pygame.K_SPACE:
            self._fire_bullets()

    def _check_keyup_events(self, event):
        """Actions responding to key up"""
        if event.key == pygame.K_RIGHT :
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT :
            self.ship.moving_left = False

    def _fire_bullets(self):
        """create a new bullet and add it to bullets group"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self) # need to pass in self as ai_game
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """private fn:  update screen"""
        # draw/render but not make it visible
        self.screen.fill(self.bg_color)
        # draw image onto screen
        self.ship.blitme()
        # draw a group of bullets using
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Flip - Render screen by making drawing visible
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()