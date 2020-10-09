import sys
import time

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats

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

        # initiate game - a ship, bullets, aliens
        self.stats = GameStats(self)
        self.ship = Ship(self)
        # create a group of bullets
        self.bullets = pygame.sprite.Group()
        # create a group of alien ships
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """Start main loop of the game"""
        while True:
            # to listen to keystroke events
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

    def _update_bullets(self):
        """update position of bullets and remove bullets when they
        pass top of screen"""
        self.bullets.update()
        for bullet in self.bullets.copy() :
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)
        self._check_bullet_hit_alien()


    def _check_bullet_hit_alien(self):
        """if bullets hit aliens, remove them"""
        # groupcollide() checks if there's collisions between groupA, groupB,
        # if True will remove them.  Returns a dict{groupA: groupB}
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # repopulate aliens if none left and reset bullets to 0
        if not self.aliens:  # empty
            self.bullets.empty()  # empty is a sprite method
            self._create_fleet()

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

    def _create_fleet(self):
        """create a fleet of alien ships"""
        # create an alien to get its attr for spacing aliens in a row.
        alien = Alien(self)
        avail_space_x = self.settings.screen_width - (2 * alien.width)
        number_aliens_x = avail_space_x // (2 * alien.width)

        # determine number of rows aliens can fit into height of screen\
        # each alien needs margin of height on top and bottom, plus another
        # row to give player more room
        avail_space_y = self.settings.screen_height - (3 * alien.height) \
                        - alien.height
        number_rows = avail_space_y // (2 * alien.height)

        # actually create rows of aliens here
        for row in range(number_rows):
            for col in range(number_aliens_x):
                self._create_alien(row, col)

    def _create_alien(self, row, col):
        alien = Alien(self)
        # set x coord of alien = left margin + (2 * alien.width)
        alien.rect.x = alien.width + (2 * alien.width) * col
        # alien.rect.x = alien.x
        # set y = top margin + (2 * height) * row
        alien.rect.y = alien.height + (2 * alien.height) * row
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """if any alien hits screen eddge, takes proper actions"""
        for alien in self.aliens.sprites():
            if alien.check_edge():
                # take these actions
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop entire fleet down, and change fleet direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_speedy
        self.settings.fleet_direction *= -1  # flip fleet direction

    def _update_aliens(self):
        """if fleet is at screen edge, update pos of all aliens
        the first changes y position, and then use aliens.update to
        update x pos"""
        self._check_fleet_edges()
        self.aliens.update()
        # check if ship collides with any aliens
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _ship_hit(self):
        """actions when ship is hit"""
        self.stats.ship_left -= 1
        self.bullets.empty()
        self.aliens.empty()
        self._create_fleet()
        self.ship.center_ship()

        #time pause
        time.sleep(0.5)

    def _update_screen(self):
        """private fn:  update screen"""
        # draw/render but not make it visible
        self.screen.fill(self.bg_color)
        # draw image onto screen
        self.ship.blitme()
        # draw a group of bullets using
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # draw aliens
        self.aliens.draw(self.screen)
        # Flip - Render screen by making drawing visible
        pygame.display.flip()

if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()