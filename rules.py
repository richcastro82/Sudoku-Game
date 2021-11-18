# Richard Castro
# November 2021
# Rules file for the Sudoku game

import pygame
from vars import *
#
# class Board:
#     def __init__(self, width, height, margin, size):
#


def drawGrid(height, width, margin, gridBox):

    for x in range(height):
        for y in range(width):
            rect=pygame.Rect(x*(gridBox+margin), y*(gridBox+margin), gridBox, gridBox)
            pygame.draw.rect(screen, grid_lines, rect)
