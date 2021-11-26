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
    # Main game loop
    while True:
        clock.tick(fps)
        screen.fill(peach)
        drawLine()
        pygame.display.update()
        # Event Handling
        for event in pygame.event.get():
            # Quit via close button
            if event.type == pygame.QUIT:
                game_over()

        # drawGrid(height, width, lines, gridBox)


if __name__ == '__main__':
    sudoku()
