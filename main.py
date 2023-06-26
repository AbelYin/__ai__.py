import pygame

from __board__ import Board
from __game_work__ import Work
from __settings__ import Settings
from __data__ import Data
from __victory__ import Victory
from __ai__ import Ai
import sys
import time


def start_game():
    """初始化程序"""
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width,
                                      settings.screen_height))
    data = Data()
    board = Board(settings, screen)
    win = Victory(settings, screen)
    ai = Ai(data,settings,screen)
    work = Work(data, settings, screen, board, win , ai)

    work.add_all_chess()
    while settings.game_active:
        screen.fill(settings.bg_color)
        work.draw_all()
        work.check_chess_eat()
        pygame.display.flip()
        work.check_events()
    work.game_end(data.game_loser)
    pygame.display.flip()
    time.sleep(2)
    sys.exit()


start_game()
