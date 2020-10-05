import pygame

class Alien(pygame.sprite.Sprite):
    """A class to manage the ship"""
    def __init__(self, ai_game):
        """Initiate parent class - if you don't do "from pygame.sprite
        import Sprite need to specify the parent class instead super()"""
        pygame.sprite.Sprite.__init__(self)
        """Initialize the ship and set its starting position"""
        # get screen from ai_game
        self.screen = ai_game.screen
        # get settings from ai_game
        self.settings = ai_game.settings
        # get rect attr from ai_game screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load alien image and convert to bmp
        self.image = pygame.image.load('images/yellow_alien.png').convert()
        # resize with 0 rotation, and 0.35 scale
        self.image = pygame.transform.rotozoom(self.image, 0, 0.35)
        # make bg_color of alien transparent
        self.image.set_colorkey(self.settings.alien_bg_color)
        # get ship position (x,y)
        self.rect = self.image.get_rect()

        # start each new alien ship at the top left of screen
        self.rect.topleft = self.screen_rect.topleft
        # get ship x position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # # set initial key stroke state
        # self.moving_right = False
        # self.moving_left = False
        # self.moving_up = False

    # def update(self):
    #     """update ship position based on movement flag"""
    #     # before each move, check if ship is inside screen
    #     if self.x <= self.screen.screen_width():
    #         self.x += self.settings.ship_speed
    #     else:
    #         self.y += self.rect.height()
        self.rect.x = self.x

    # def blitme(self):
    #     """draw ship onto screen by copying pixel from image to position"""
    #     self.screen.blit(self.image, self.rect)
