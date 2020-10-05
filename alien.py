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
        self.image = pygame.transform.rotozoom(self.image, 0, 0.4415)
        # make bg_color of alien transparent
        self.image.set_colorkey(self.settings.alien_bg_color)
        # get ship position (x,y)
        self.rect = self.image.get_rect()

        # alien width and height
        self.width = self.rect.width
        self.height = self.rect.height

        # start each new alien ship at the top left of screen with margin
        # 1 width to right and 1 height down.  (x,y) have to be int
        self.rect.x = int(self.width)
        self.rect.y = int(self.height)

        # get alien ship x,y positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    # def update(self):
    #     """move alien to right until it disappears from screen"""
