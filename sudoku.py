# Richard Castro
# November 2021
# Sudoku game built with pygame I used pygame libraries to build
# the Conway's Game of Life and decided to create one of my favorite game with
# what I learned about pygame before I forget most of it. just like the game of
# life, sudoku uses a grid board of sqaure tiles and mouse grid localization.
# I will have to learn a little more about pygame while creating the rules file
# for this sudoku game and that will probably lead to me making some changes
# to the conway game.

# Import libraries
import pygame, os
from rules import *
from vars import *
import sys, os
# Initialize the game
clock=pygame.time.Clock()


pygame.init()

pygame.display.set_caption('Richard Castro - Sudoku Game')


def sudoku():
    while True: #main game loop
        clock.tick(fps)
        screen.fill(grid_bg)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        drawGrid(height, width, margin, gridBox)

        pygame.display.update()

if __name__ == '__main__':
    sudoku()
