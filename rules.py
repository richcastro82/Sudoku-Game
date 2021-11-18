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


def drawLine():
    pygame.draw.line(screen, blk, [x, y], [x,y+600], 4)
    pygame.draw.line(screen, blk, [x+gridSq, y], [x+gridSq,y+600], 4)
    pygame.draw.line(screen, blk, [x, y], [x+600,y], 4)
    pygame.draw.line(screen, blk, [x, y+gridSq], [x+600,y+gridSq], 4)
