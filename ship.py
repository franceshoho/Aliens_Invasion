import pygame

class Ship:
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position"""
        # get screen from ai_game
        self.screen = ai_game.screen
        # get settings from ai_game
        self.settings = ai_game.settings
        # get rect attr from ai_game screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        # get ship position (x,y)
        self.rect = self.image.get_rect()

        # start each new ship at the bottom center of screen
        self.center_ship()

        # set initial key stroke state
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False

    def update(self):
        """update ship position based on movement flag"""
        # before each move, check if ship is inside screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        # update ship position
        self.rect.x = self.x

    def blitme(self):
        """draw ship onto screen by copying pixel from image to position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
