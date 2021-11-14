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
import pygame

# Screen settings
width=600
height=600
size=(width, height)

# Grid settings
Black=(0,0,0)
White=(255,255,255)
Grey=(100,100,100)

# Initialize the game
pygame.init()
screen=pygame.display.set_mode(size)
pygame.display.set_caption('Richard Castro - Sudoku Game')

while True: #main game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
