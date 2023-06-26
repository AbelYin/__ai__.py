from pygame.sprite import Group


class Data:
    """存储游戏中产生的数据"""

    def __init__(self):
        self.board = [["" for i in range(0, 10)] for j in range(0, 9)]  # 棋盘
        self.black_chess = Group()
        self.red_chess = Group()
        self.av_move = Group()
        self.chess_add = ["黑将", "黑相", "黑相", "黑兵", "黑兵", "黑兵", "黑兵", "黑兵", "黑马", "黑马", "黑车",
                          "黑车", "黑炮", "黑炮", "黑士", "黑士", "红将", "红相", "红相",
                          "红兵", "红兵", "红兵", "红兵", "红兵", "红马",
                          "红马", "红车", "红车", "红炮", "红炮", "红士", "红士", ]
        self.a_m_t = [4, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 4, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2]
        self.chess_x = [4, 2, 6, 2, 6, 0, 8, 4, 1, 7, 0, 8, 1, 7, 3, 5, 4, 2, 6, 0, 2, 4, 6, 8, 1, 7, 0, 8, 1, 7, 3, 5]
        self.chess_y = [0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 2, 2, 0, 0, 9, 9, 9, 6, 6, 6, 6, 6, 9, 9, 9, 9, 7, 7, 9, 9]
        self.move_to = {'将': [[0, 50, 0, -50], [50, 0, -50, 0]],
                        '相': [[100, 100, -100, -100], [100, -100, 100, -100]],
                        '黑兵': [[0, 50, -50], [50, 0, 0]],
                        '马': [[100, 100, 50, -50, -100, -100, 50, -50], [50, -50, 100, 100, 50, -50, -100, -100]],
                        '车': self.make_car_chess(), '炮': self.make_car_chess(),
                        '士': [[50, 50, -50, -50], [50, -50, -50, 50]], '红兵': [[0, 50, -50], [-50, 0, 0]]}
        # 棋子可以到达的点
        self.now_chess = 0
        # 是否有移动限制（马腿，相眼）
        self.horse_av = [[1, 1, 0, 0, -1, -1, 0, 0], [0, 0, 1, 1, 0, 0, -1, -1]]
        self.xiang_av = [[1, 1, -1, -1], [1, -1, 1, -1]]
        self.move_av = [0, self.xiang_av, self.xiang_av, 0, 0, 0, 0, 0, self.horse_av, self.horse_av, 0, 0, 0, 0, 0, 0,
                        0, self.xiang_av, self.xiang_av, 0, 0, 0, 0, 0, self.horse_av, self.horse_av, 0, 0, 0, 0, 0, 0]
        # 攻击方式（0为直接吃，1为隔子吃）
        self.chess_eat = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0]

        # 轮次
        self.now_player = -1  # 1是红，-1是黑
        # 游戏状态
        self.game_loser = ""


    def make_car_chess(self):
        # 生成车的行动参数
        to_x = []
        to_y = []
        for i in range(0, -501, -50):
            if i == 0:
                continue
            to_x.append(i)
            to_y.append(0)
        for i in range(0, 501, 50):
            if i == 0:
                continue
            to_x.append(i)
            to_y.append(0)
        for i in range(0, -501, -50):
            if i == 0:
                continue
            to_x.append(0)
            to_y.append(i)
        for i in range(0, 501, 50):
            if i == 0:
                continue
            to_x.append(0)
            to_y.append(i)
        return [to_x, to_y]
