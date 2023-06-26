import pygame
from pygame.sprite import Sprite


class MoveAv(Sprite):
    """一个模拟棋子可以到达的点的类"""

    def __init__(self,  setting, screen, x, y):
        super(MoveAv,self).__init__()
        # 外部数据引入
        self.setting = setting
        self.screen = screen
        self.x = x  # 棋盘上x坐标
        self.y = y  # 棋盘上y坐标
        # 绘图数据
        self.image = pygame.image.load(r"棋子/可行动点.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.x * 50 + 45
        self.rect.y = self.y * 50 + 45

    def show(self):
        # 绘制
        self.screen.blit(self.image, self.rect)
