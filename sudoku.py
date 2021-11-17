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
import pygame, sys
# Screen settings
size=(600,600)
margin=1
grid_bg=(239,239,239)
grid_lines=(100,100,100)
grid_borders=(0,0,0)
clock=pygame.time.Clock()
fps=15

gridW=10
gridH=10
gridBox=(gridW,gridH)
# Initialize the game
pygame.init()
screen=pygame.display.set_mode(size)
pygame.display.set_caption('Richard Castro - Sudoku Game')

while True: #main game loop
    clock.tick(fps)
    screen.fill(grid_bg)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.draw.rect(screen, grid_lines, (1,1,25,25))


    pygame.display.update()
