import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """管理星星的类"""

    def __init__(self, ai_game):
        """初始化星星属性设置"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('image/star.bmp')
        self.rect = self.image.get_rect()

        #x ，y分别表示离屏幕左边缘和上边缘的距离
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)


