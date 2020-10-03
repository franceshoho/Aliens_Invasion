import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        self.screen = ai_game.screen
        # get attr of rect for rocket pos
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of screen
        self.rect.midbottom = self.screen_rect.midbottom
        # set initial key stroke state
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False


    def update(self):
        """update ship position based on movement flag"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1



    def blitme(self):
        """draw ship onto screen by copying pixel from image to position"""
        self.screen.blit(self.image, self.rect)
