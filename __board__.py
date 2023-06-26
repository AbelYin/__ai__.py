import pygame
from pygame.sprite import Sprite


class Board(Sprite):
    """底部棋盘"""
    def __init__(self, ai_settings, screen):
        super(Board, self).__init__()
        # 外部继承
        self.screen = screen
        self.ai_settings = ai_settings
        # 基本展示参数
        self.image = pygame.image.load(r'棋子\棋盘.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def show(self):
        # 绘制
        self.screen.blit(self.image, self.rect)
