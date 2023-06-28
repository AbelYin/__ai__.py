import copy

import pygame
import sys
from __move_avaliable__ import MoveAv
from __chess__ import Chess


class Work:

    def __init__(self, data, setting, screen, board, win, ai):
        """游戏运行时需要的函数"""
        self.data = data
        self.setting = setting
        self.screen = screen
        self.board = board
        self.win = win
        self.ai = ai

    def check_events(self):
        """检查所有游戏事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 退出事件
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # 鼠标按下事件
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(self.ai.score())
                self.check_chess_click(mouse_x, mouse_y)  # 检查所有棋子是否按下
                self.check_moveav_click(mouse_x, mouse_y)

    def check_chess(self, xa, ya, xb, yb):
        # 检查两个点之间有几个子
        xa = int(xa)
        ya = int(ya)
        xb = int(xb)
        yb = int(yb)
        ans = 0

        for i in range(min(xa, xb), max(xa, xb) + 1):
            for j in range(min(ya, yb), max(ya, yb) + 1):
                if i == xa and j == ya:
                    continue
                if i == xb and j == yb:
                    continue
                if self.data.board[i][j] != "":
                    ans += 1

        return ans

    def check_allowed_move(self, moveav, chess_e, i):
        # 外部数据导入
        x = moveav.x * 50 + 50
        y = moveav.y * 50 + 50
        z = chess_e.a_m_t
        # 特殊判定（小兵）
        if chess_e.name[1] == '兵':
            if chess_e.name[0] == '红':
                if chess_e.y > 4 and chess_e.y == int(moveav.y):
                    return 0
            else:
                if chess_e.y < 5 and chess_e.y == int(moveav.y):
                    return 0

        # 检查将帅对立

        # 获取将帅坐标
        for i in self.data.black_chess:
            if i.name[1] == '将':
                ya = i.y
                xa = i.x
        for i in self.data.red_chess:
            if i.name[1] == '将':
                yb = i.y
                xb = i.x

        # 判定
        if xa == xb and chess_e.name[1] != '将':
            if chess_e.x == xa and moveav.x != xa:
                if self.check_chess(xa, ya, xb, yb) == 1:
                    return 0
        if chess_e.name[1] == '将' and xa == xb:
            if chess_e.name[0] == '红':
                if self.check_chess(xa, ya, moveav.x, moveav.y) == 0:
                    return 0
            else:
                if self.check_chess(moveav.x, moveav.y, xb, yb) == 0:
                    return 0
        # 离开棋盘
        if not (50 <= x <= 450 and 50 <= y <= 500):
            return 0
        # 重叠
        try:
            if self.data.board[int((x - 50) / 50)][int((y - 50) / 50)][0] == chess_e.name[0]:
                return 0
        except IndexError:
            pass
        # 移动范围限制
        if z == 1:
            # 黑方区域
            if y < 300:
                return 0
        elif z == 2:
            # 红方皇宫
            if not 200 <= x <= 300:
                return 0
            if not 400 <= y <= 500:
                return 0
        elif z == 3:
            # 红方区域
            if y > 300:
                return 0
        elif z == 4:
            # 黑方皇宫
            if not 200 <= x <= 300:
                return 0
            if not 50 <= y <= 150:
                return 0

        # 特殊判定（炮吃子）
        try:
            if self.data.board[int((x - 50) / 50)][int((y - 50) / 50)][0] != chess_e.name[0] and self.check_chess(
                    chess_e.x, chess_e.y, moveav.x,
                    moveav.y) == 1 and chess_e.name[1] == '炮':
                return 1

        except IndexError:
            pass

        # 特殊判定（车，炮移动）

        try:
            if self.check_chess(
                    chess_e.x, chess_e.y, moveav.x,
                    moveav.y) == 0 and (
                    chess_e.name[1] == '车'):
                return 1
            else:
                if chess_e.name[1] == '车':
                    return 0

        except IndexError:
            pass

        try:

            if self.check_chess(
                    chess_e.x, chess_e.y, moveav.x,
                    moveav.y) == 0 and (
                    chess_e.name[1] == '炮' and self.data.board[int(moveav.x)][int(moveav.y)] == ""):
                return 1
            else:
                if chess_e.name[1] == '炮':
                    return 0

        except IndexError:
            pass

        # 特殊判定（马腿，相眼）
        try:

            if chess_e.move_av != 0:
                ii = chess_e.to[0].index(moveav.x * 50 - chess_e.x * 50)
                if self.data.board[chess_e.x + chess_e.move_av[0][ii]][chess_e.y + chess_e.move_av[1][ii]] != "":
                    return 0
                pass

        except IndexError:
            pass

        return 1

    def make_av_move(self, chess_e):
        """生成可移动点"""
        self.data.now_chess = chess_e
        self.data.av_move.empty()
        for ia in range(0, len(chess_e.to[0])):
            a = MoveAv(self.setting, self.screen, chess_e.x + chess_e.to[0][ia] / 50, chess_e.y + chess_e.to[1][ia] / 50)
            # 判断点是否合法
            if self.check_allowed_move(a, chess_e, ia):
                self.data.av_move.add(a)


    def game_end(self, loser):
        # 结束游戏
        if loser == '红':
            self.win.show_a()
        else:
            self.win.show_b()


    def check_moveav_click(self, x, y):
        # 检查data中av_move的点击
        for i in self.data.av_move:
            if i.rect.collidepoint(x, y):
                try:
                    flag = self.data.board[int(i.x)][int(i.y)]
                    if flag[1] == "将":
                        self.data.game_loser = flag[0]
                        self.setting.game_active = False
                except IndexError:
                    pass
                self.data.now_chess.move_to(i.x, i.y)
                print(self.ai.score())
                self.data.av_move.empty()
                self.data.now_player *= -1


    def check_chess_click(self, x, y):
        if self.data.now_player == -1:
            # 检查红棋
            for i in self.data.red_chess:
                if i.rect.collidepoint(x, y):
                    self.make_av_move(i)
        else:
            for i in self.data.black_chess:
                if i.rect.collidepoint(x, y):
                    self.make_av_move(i)
            # 检查黑棋

            a = copy.deepcopy(self.data.board)
            self.ai.HistoryTable = {}
            self.ai.MaxMin(2)
            print("ans:",self.ai.best_move)
            print("now:",self.ai.score())
            self.data.board = copy.deepcopy(a)

            for i in self.data.black_chess:
                if i.x == self.ai.best_move[0] and i.y == self.ai.best_move[1]:
                    i.move_to(self.ai.best_move[2],self.ai.best_move[3])
            self.data.now_player *=-1




    def draw_all(self):
        self.screen.fill(self.setting.bg_color)
        self.board.show()
        self.data.black_chess.draw(self.screen)
        self.data.red_chess.draw(self.screen)
        self.data.av_move.draw(self.screen)

    def add_all_chess(self):
        """添加所有象棋棋子"""
        for i in range(0, len(self.data.chess_add)):
            # 象棋棋子数据
            a = self.data.chess_add[i]
            b = self.data.chess_x[i]
            c = self.data.chess_y[i]
            # 特判
            if a[1] != '兵':
                e = self.data.move_to[a[1]]
            else:
                e = self.data.move_to[a]
            # 棋子精灵生成
            f = self.data.a_m_t[i]
            g = self.data.move_av[i]
            h = self.data.chess_eat[i]
            d = Chess(a, self.setting, self.screen, b, c, e, f, self.data, g, h)
            # 根据精灵类别加入不同的组
            if a[0] == '黑':
                self.data.black_chess.add(d)
            else:
                self.data.red_chess.add(d)

    def check_chess_eat(self):
        # 根据轮次删除被吃的子
        if self.data.now_player == 1:
            pygame.sprite.groupcollide(self.data.red_chess, self.data.black_chess, False, True)
        else:
            pygame.sprite.groupcollide(self.data.red_chess, self.data.black_chess, True, False)
