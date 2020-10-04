import pygame
from pygame.sprite import Sprite
# Sprite groups objects into a list and will do all update() for
# objs in group

class Bullet(Sprite):
    """A class to manage a group of bullets fired from ship"""
    def __init__(self, ai_game):
        # inherit from class Sprite
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # create bullet as rect at (0,0) with width, height in settings
        self.rect = pygame.Rect(0, 0,self.settings.bullet_width,
                                self.settings.bullet_height)
        # then reset bullet pos to midtop of ship
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullet's position as decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up the screen"""
        # bullet is going up so need to decrease y
        self.y -= self.settings.bullet_speed
        # update bullet pos
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet to screen"""
        pygame.draw.rect(self.screen, color=self.color,
                         rect=self.rect)