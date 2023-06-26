import pygame
from pygame.sprite import Sprite


class Chess(Sprite):
    """一个模拟棋子的类"""

    def __init__(self, name, setting, screen, x, y, to, av_move_through, data, move, way_of_eat):
        super(Chess, self).__init__()
        # 外部数据引入
        self.name = name
        self.setting = setting
        self.screen = screen
        self.x = x  # 棋盘上x坐标
        self.y = y  # 棋盘上y坐标
        self.to = to  # 可移动点
        self.a_m_t = av_move_through  # 存储移动范围限制（0：无，1：红方区域，2：红方皇宫，3：黑方区域，4：黑方皇宫）
        self.data = data
        self.data.board[x][y] = self.name
        self.move_av = move  # 是否有移动限制
        self.eat = way_of_eat  # 吃子方式
        # 绘图数据
        self.image = pygame.image.load(r"棋子" + r"/" + self.name + ".png")
        self.rect = self.image.get_rect()
        self.rect.x = self.x * 50 + 25
        self.rect.y = self.y * 50 + 25

    def show(self):
        # 绘制
        self.screen.blit(self.image, self.rect)

    def move_to(self, x, y):
        # 坐标更新
        x = int(x)
        y = int(y)
        self.data.board[self.x][self.y] = ""
        self.x = x
        self.y = y
        self.data.board[x][y] = self.name
        # 地图坐标更新
        self.rect.x = self.x * 50 + 25
        self.rect.y = self.y * 50 + 25
