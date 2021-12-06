# Richard Castro
# November 2021
# Rules file for the Sudoku game

import pygame,sys
from vars import *


class Button:
    def __init(self, x, y, w, h, text=""):
        self.x=x
        self.y=y
        self.width=w
        self.height=h
        self.text=text

    def DrawButton(self):
        pass

    def isOver(self, pos):
        pass


class Board:
    def __init__(self, width, height, lines, size):
        self.width=width
        self.height=height
        self.lines=lines
        self.size=size

    def StartMenu(self):
        bg=pygame.image.load('bg.png')
        START_BUT=Button(10,10,40,80,"Start Game")
        QUIT_BUT=Button(20,20,40,80,"Quit Game")
        START_BUT.DrawButton()
        QUIT_BUT.DrawButton()
        run_game=False
        while run_game==False:
            screen.blit(bg, (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    run_game=True

    def PauseScreen(self):
        pass

    def QuitGame(self):
        pygame.quit()
        sys.exit()

    def GridLines(self):
        for x in range(0,self.width,self.size):
            for y in range(0,self.height,self.size):
                pygame.draw.line(screen, reddish, [x,y],[x, y+self.width],2)
                pygame.draw.line(screen, reddish, [x, y], [x+self.height, y], 2)
