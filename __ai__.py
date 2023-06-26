import copy

from __move_avaliable__ import MoveAv


class Ai:
    """
    象棋ai
    """

    def __init__(self, data, settings, screen):
        # 子在不同位置的价值
        # 帅
        self.chess_place_a = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [11, 2, 1, 0, 0, 0, 0, 1, 2, 11],
                              [15, 2, 1, 0, 0, 0, 0, 1, 2, 15],
                              [11, 2, 1, 0, 0, 0, 0, 1, 2, 11],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        # 士
        self.chess_place_b = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [20, 0, 20, 0, 0, 0, 0, 20, 0, 20],
                              [0, 23, 0, 0, 0, 0, 0, 0, 23, 0],
                              [20, 0, 20, 0, 0, 0, 0, 20, 0, 20],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        # 相
        self.chess_place_c = [[0, 0, 18, 0, 0, 0, 0, 18, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [20, 0, 0, 0, 20, 20, 0, 0, 0, 20],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 23, 0, 0, 0, 0, 23, 0, 0],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [20, 0, 0, 0, 20, 20, 0, 0, 0, 20],
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                              [0, 0, 18, 0, 0, 0, 0, 18, 0, 0]]
        # 马
        self.chess_place_d = [[88, 85, 93, 92, 90, 90, 93, 92, 90, 90],
                              [85, 90, 92, 94, 98, 100, 108, 98, 96, 90],
                              [90, 92, 94, 98, 101, 99, 100, 99, 103, 90],
                              [88, 93, 95, 95, 102, 103, 107, 103, 97, 96],
                              [90, 87, 92, 98, 103, 104, 100, 99, 94, 90],
                              [88, 93, 95, 95, 102, 103, 107, 103, 97, 96],
                              [90, 92, 94, 98, 101, 99, 100, 99, 103, 90],
                              [85, 90, 92, 94, 98, 100, 108, 98, 96, 90],
                              [88, 85, 93, 92, 90, 90, 93, 92, 90, 90]]
        # 车
        self.chess_place_e = [[194, 200, 198, 204, 208, 208, 206, 206, 206, 206],
                              [206, 208, 208, 209, 212, 211, 213, 208, 212, 208],
                              [204, 206, 204, 204, 212, 211, 213, 207, 209, 207],
                              [212, 212, 212, 212, 214, 214, 216, 214, 216, 213],
                              [200, 200, 212, 214, 215, 215, 216, 216, 233, 214],
                              [212, 212, 212, 212, 214, 214, 216, 214, 216, 213],
                              [204, 206, 204, 204, 212, 211, 213, 207, 209, 207],
                              [206, 208, 208, 209, 212, 211, 213, 208, 212, 208],
                              [194, 200, 198, 204, 208, 208, 206, 206, 206, 206]]
        # 炮
        self.chess_place_f = [[96, 96, 97, 96, 95, 96, 96, 97, 98, 100],
                              [96, 97, 96, 96, 96, 96, 99, 97, 98, 100],
                              [97, 98, 100, 96, 99, 96, 99, 96, 96, 96],
                              [99, 98, 99, 96, 96, 96, 98, 91, 92, 91],
                              [99, 98, 101, 96, 100, 100, 100, 92, 89, 90],
                              [99, 98, 99, 96, 96, 96, 98, 91, 92, 91],
                              [97, 98, 100, 96, 99, 96, 99, 96, 96, 96],
                              [96, 97, 96, 96, 96, 96, 99, 97, 98, 100],
                              [96, 96, 97, 96, 95, 96, 96, 97, 98, 100]]
        # 兵
        self.chess_place_g = [[0, 0, 0, 7, 7, 14, 19, 19, 19, 9],
                              [0, 0, 0, 0, 0, 18, 23, 24, 24, 9],
                              [0, 0, 0, 7, 13, 20, 27, 32, 34, 9],
                              [0, 0, 0, 0, 0, 27, 29, 37, 42, 11],
                              [0, 0, 0, 15, 16, 29, 30, 37, 44, 13],
                              [0, 0, 0, 0, 0, 27, 29, 37, 42, 11],
                              [0, 0, 0, 7, 13, 20, 27, 32, 34, 9],
                              [0, 0, 0, 0, 0, 18, 23, 24, 24, 9],
                              [0, 0, 0, 7, 7, 14, 19, 19, 19, 9]]
        # 打分数据
        self.next_move = []
        self.HistoryTable = {}
        self.best_move = 1000
        self.flag = False
        self.chess_move_score = {'将': self.chess_place_a, '相': self.chess_place_c, '兵': self.chess_place_g,
                                 '车': self.chess_place_e, '炮': self.chess_place_f, '士': self.chess_place_b,
                                 '马': self.chess_place_d,}

        # 外部引用
        self.data = data
        self.setting = settings
        self.screen = screen

    def encode(self, chess_e, moveav):
        # 压缩移动
        return int(moveav.y + 10 * moveav.x + 100 * chess_e.y + 1000 * chess_e.x)

    def decode(self, x):
        # 解压移动
        ans = [int(x / 1000), int((x % 1000 / 100)), int((x % 100) / 10), int(x % 10)]
        return ans

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

    def check_move(self, moveav, chess_e, i):
        # 检查移动是否合法
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

    def make_next_chess_move(self, mode):
        # 根据局面生成接下来的所有移动
        self.next_move = []
        if mode:
            for chess_e in self.data.red_chess:
                for ia in range(0, len(chess_e.to[0])):
                    a = MoveAv(self.setting, self.screen, chess_e.x + chess_e.to[0][ia] / 50,
                               chess_e.y + chess_e.to[1][ia] / 50)
                    # 判断点是否合法
                    if self.check_move(a, chess_e, ia):
                        self.next_move.append(self.encode(chess_e, a))
        else:
            for chess_e in self.data.black_chess:
                for ia in range(0, len(chess_e.to[0])):
                    a = MoveAv(self.setting, self.screen, chess_e.x + chess_e.to[0][ia] / 50,
                               chess_e.y + chess_e.to[1][ia] / 50)
                    # 判断点是否合法
                    if self.check_move(a, chess_e, ia):
                        self.next_move.append(self.encode(chess_e, a))

    def score(self):
        """
        这是对局面的评价函数
        评价标准
        1.棋子价值
        2.形状
        3.图案
        4.威胁
        :return:
        """
        ans = 0
        # 威胁

        # 棋子价值 + 图案
        for i in range(9):
            for k in range(10):
                j = self.data.board[i][k]
                if j != "":
                    if j[0] == '红':
                        # print(j, self.chess_move_score[j[1]][i][k])
                        ans -= self.chess_move_score[j[1]][i][k]
                    else:
                        # print(j, self.chess_move_score[j[1]][8-i][9-k])
                        ans += self.chess_move_score[j[1]][8-i][9-k]
        # 形状
        # 窝心马
        if self.data.board[4][1] == "黑马":
            ans -= 2000
        if self.data.board[4][8] == "红马":
            ans += 2000
        # 空头炮
        for i in self.data.black_chess:
            if i.name[1] == '将':
                ya = i.y
                xa = i.x
        for i in self.data.red_chess:
            if i.name[1] == '将':
                yb = i.y
                xb = i.x
        for i in range(ya + 1, 10):
            if self.data.board[xa][i] != "":
                if self.data.board[xa][i] == '红炮':
                    ans -= 2000
                break

        for i in range(yb - 1, 0, -1):
            if self.data.board[xb][i] != "":
                if self.data.board[xb][i] == '黑炮':
                    ans += 2000
                break

        return ans

    def move(self, x):
        a = self.decode(x)
        self.data.board[a[2]][a[3]] = self.data.board[a[0]][a[1]]
        self.data.board[a[0]][a[1]] = ''

    def check_checkmate(self, dp):
        self.make_next_chess_move(dp % 2)
        self.next_move_b = copy.deepcopy(self.next_move)
        for i in self.data.black_chess:
            if i.name[1] == '将':
                ya = i.y
                xa = i.x
        for i in self.data.red_chess:
            if i.name[1] == '将':
                yb = i.y
                xb = i.x
        for i in self.next_move_b:
            a = self.decode(i)
            if a[2] * 10 + a[3] == xa * 10 + ya:
                return 1
            if a[2] * 10 + a[3] == xb * 10 + yb:
                return 1
        return 0

    def CompareHistory(self,elem):
        if elem in self.HistoryTable:
            return self.HistoryTable[elem]
        return 0

    def AlphaBeta(self, depth, alpha, beta,road):
        # 会自杀
        if depth == 0:
            print(road,self.score())
            return self.score()
        best = -99999999
        best_move = 0
        self.make_next_chess_move(depth % 2)
        self.next_move_a = copy.deepcopy(self.next_move)
        self.next_move_a.sort(key = self.CompareHistory)
        self.noww = copy.deepcopy(self.data.board)
        # print(self.next_move_a)
        for i in self.next_move_a:
            self.move(i)
            road.append(i)
            if self.check_checkmate(depth):
                self.data.board = copy.deepcopy(self.noww)
            else:
                print(depth,':',i,":",self.score(),best)
                now = -self.AlphaBeta(depth - 1, -beta, -alpha,road)
                self.data.board = copy.deepcopy(self.noww)
                road.pop(-1)
                if now > best:
                    best = now
                    if now>= beta:
                        best_move = self.decode(i)
                        break
                    if now> alpha:
                        best_move = self.decode(i)
                        alpha = now

        if best == -99999999:
            return 99999999 + depth*100
        if best_move != 0 :
            if i in self.HistoryTable:
                self.HistoryTable[i] += depth*depth
            else:
                self.HistoryTable[i] = depth*depth
            if depth == 4:
                self.best_move = best_move
        return alpha
