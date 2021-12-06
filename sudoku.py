# Richard Castro
# November 2021
# Sudoku game built with pygame I used pygame libraries to build
# the Conway's Game of Life and decided to create one of my favorite game with
# what I learned about pygame before I forget most of it. just like the game of
# life, sudoku uses a grid board of sqaure tiles and mouse grid localization.
# I will have to learn a little more about pygame while creating the rules file
# for this sudoku game and that will probably lead to me making some changes
# to the conway game.

import pygame, os, sys
from rules import *
from vars import *

pygame.init()
clock=pygame.time.Clock()
pygame.display.set_caption('Richard Castro - Sudoku Game')

def sudoku():
    RUNTIME=Board(width, height,sqaure,66)
    RUNTIME.StartMenu()
    while True:
        screen.fill(peach)
        RUNTIME.GridLines()
        clock.tick(fps)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNTIME.QuitGame()


if __name__ == '__main__':
    sudoku()
