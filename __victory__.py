import pygame
from pygame.sprite import Sprite


class Victory(Sprite):
    """底部棋盘"""
    def __init__(self, ai_settings, screen):
        super(Victory, self).__init__()
        # 外部继承
        self.screen = screen
        self.ai_settings = ai_settings
        # 基本展示参数
        self.image = pygame.image.load(r'棋子\黑方胜利.bmp')
        self.image_a = pygame.image.load(r'棋子\红方胜利.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 25

    def show_a(self):
        # 绘制黑方胜利
        self.screen.blit(self.image, self.rect)

    def show_b(self):
        # 绘制红方胜利
        self.screen.blit(self.image_a, self.rect)
