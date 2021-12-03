# Richard Castro
# November 2021
# Rules file for the Sudoku game

import pygame
from vars import *
#
# class Board:
#     def __init__(self, width, height, lines, size):
#

# def drawGrid(width, height, lines, gridBox):
#     for x in range(height):
#         for y in range(width):
#             rect=pygame.Rect(x*(gridBox+lines), y*(gridBox+lines), gridBox, gridBox)
#             pygame.draw.rect(screen, lines, rect)


def home_screen():
    pass

def game_over():
    pygame.quit()

def drawLine():
    for x in range (0, 600, 66 ):
        for y in range(0,600,66):
            pygame.draw.line(screen, reddish, [x,y],[x,y+width], 4)
            pygame.draw.line(screen, reddish, [x,y],[x+height,y], 4)
    # Need to loop this code
    # pygame.draw.line(screen, reddish, [x, y], [x,y+600], 4)
    # pygame.draw.line(screen, reddish, [x+gridBox, y], [x+gridBox,y+600], 4)
    # pygame.draw.line(screen, reddish, [x+gridBox*2, y], [x+gridBox*2,y+600], 4)
    # pygame.draw.line(screen, reddish, [x+gridBox*3, y], [x+gridBox*3,y+600], 4)
    # pygame.draw.line(screen, reddish, [x+gridBox*4, y], [x+gridBox*4,y+600], 4)
    # pygame.draw.line(screen, reddish, [x+gridBox*5, y], [x+gridBox*5,y+600], 4)
    # pygame.draw.line(screen, reddish, [x+gridBox*6, y], [x+gridBox*6,y+600], 4)
    # pygame.draw.line(screen, reddish, [x+gridBox*7, y], [x+gridBox*7,y+600], 4)
    # pygame.draw.line(screen, reddish, [x+gridBox*8, y], [x+gridBox*8,y+600], 4)
    # pygame.draw.line(screen, reddish, [x+gridBox*9, y], [x+gridBox*9,y+600], 4)
    #
    # pygame.draw.line(screen, reddish, [x, y+gridBox], [x+600,y+gridBox], 4)
    # pygame.draw.line(screen, reddish, [x, y+gridBox*2], [x+600,y+gridBox*2], 4)
    # pygame.draw.line(screen, reddish, [x, y+gridBox*3], [x+600,y+gridBox*3], 4)
    # pygame.draw.line(screen, reddish, [x, y+gridBox*4], [x+600,y+gridBox*4], 4)
    # pygame.draw.line(screen, reddish, [x, y+gridBox*5], [x+600,y+gridBox*5], 4)
    # pygame.draw.line(screen, reddish, [x, y+gridBox*6], [x+600,y+gridBox*6], 4)
    # pygame.draw.line(screen, reddish, [x, y+gridBox*7], [x+600,y+gridBox*7], 4)
    # pygame.draw.line(screen, reddish, [x, y+gridBox*8], [x+600,y+gridBox*8], 4)
    # pygame.draw.line(screen, reddish, [x, y+gridBox*9], [x+600,y+gridBox*9], 4)
