import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from ship"""
    def __init__(self, ai_game):
        """Create a bullet object at ship's current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # draw bullet as rect using pygame.Rect at (0,0)
        self.rect = pygame.Rect(left=0, top=0,
                                width=self.settings.bullet_width,
                                height=self.settings.bullet_height)
        # then reset bullet pos to midtop of ship
        self.rect.midtop = ai_game.ship.rect.midtop

        # store bullet's position as decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up the screen"""
        # bullet is going up so need to decrease y
        self.y -= self.settings.bullet_speed
        # update bullet pos
        self.rec.y = self.y

    def draw_bullet(self):
        """Draw bullet to screen"""
        pygame.draw.rect(Surface=self.screen, color=self.color,
                         Rect=self.rect)