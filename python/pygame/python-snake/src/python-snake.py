#!/usr/bin/env python

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>

    This is version 0.0.1
    
    Controls: W, A, S & D
    Escape button quits...
    Collect the fruit and avoid crashing
    
"""

import pygame, sys, random, math

from Field import Field
from Direction import Direction
from Renderer import Renderer
from Board import Board
from pygame.locals import *

# Renderer Initialization Block
pygame.init()
renderer = Renderer(pygame)

# Engine/Renderer Constants
FPS = 30                 # frames per second, the general speed of the program
DELAY=250                # time between game state changes in ms
FULLSCREEN=0             # use fullscreen mode true/false
DOUBLEBUFFER=1           # use double buffer mode true/false
HWSURFACE=1              # use a hardware surface mode true/false
DEBUG=1                  # debug mode true/false

# Game Constants
GAMENAME='Python Snake'  # name of the game to report to users
VERSION='0.5.0'          # version of the game to report to users
SEGSIZE=20               # size of a snake segment in pixels
HEADER=SEGSIZE           # The size of the score/info banner in pixels
HEADERFONTSIZE=HEADER-2  # The size of the font for score/info banner in pixels
FONT='freesansbold.ttf'  # The name of the font to use for the header
SEGX=(renderer.get_width()/SEGSIZE)-1 # The number of segments wide supported
SEGY=(renderer.get_height()/SEGSIZE)-2 # The number of segments high supported
field = Field(SEGX, SEGY)

# Game Modes
EXIT=0
PLAY=1
MENU=2

# Menu Selection
CONTINUE=0
NEWGAME=1
ENDGAME=2

pygame.display.set_caption(GAMENAME + ' ' + VERSION)
FPSCLOCK = pygame.time.Clock()
pygame.mouse.set_visible(False)

# Data Structure Initialization
board = Board(field)


def game_event_handler():
    global game_mode
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            print "Quit"
            game_mode=EXIT
        elif event.type==KEYDOWN:
            snake = board.get_snake()
            if DEBUG:
                print event
                print "Last Direction: " + str(snake.get_last_direction())
            if event.key==pygame.K_ESCAPE:
                print "Quit"
                game_mode=EXIT
            elif event.key==pygame.K_p:
                game_mode=MENU
            elif event.key==pygame.K_w or event.key==273:
                if snake.get_last_direction() != Direction.get_south():
                    snake.set_direction(Direction.get_north())
            elif event.key==pygame.K_s or event.key==274:
                if snake.get_last_direction() != Direction.get_north():
                    snake.set_direction(Direction.get_south())
            elif event.key==pygame.K_a or event.key==276:
                if snake.get_last_direction() != Direction.get_east():
                    snake.set_direction(Direction.get_west())
            elif event.key==pygame.K_d or event.key==275:
                if snake.get_last_direction() != Direction.get_west():
                    snake.set_direction(Direction.get_east())

def menu_event_handler():
    global menu_selection
    global last_menu_selection
    global game_mode
    for event in pygame.event.get(): # event handling loop
        if event.type == QUIT:
            print "Quit"
            game_mode=EXIT
        if event.type==KEYDOWN:
            if DEBUG:
                #print event
                #print "Last Direction: " + str(snake.get_last_direction())
                pass
            if event.key==pygame.K_ESCAPE:
                print "Quit"
                game_mode=EXIT
            elif event.key==pygame.K_p:
                game_mode=PLAY
            elif event.key==pygame.K_w or event.key==273:
                last_menu_selection=menu_selection
                if menu_selection==CONTINUE:
                    menu_selection=ENDGAME
                elif menu_selection==NEWGAME:
                    menu_selection=CONTINUE
                elif menu_selection==ENDGAME:
                    menu_selection=NEWGAME
            elif event.key==pygame.K_s or event.key==274:
                last_menu_selection=menu_selection
                if menu_selection==CONTINUE:
                    menu_selection=NEWGAME
                elif menu_selection==NEWGAME:
                    menu_selection=ENDGAME
                elif menu_selection==ENDGAME:
                    menu_selection=CONTINUE
            elif event.key==13:
                if menu_selection==CONTINUE:
                    game_mode=PLAY
                elif menu_selection==NEWGAME:
                    init_game()
                elif menu_selection==ENDGAME:
                    game_mode=EXIT
    

def init_game():
    global game_mode
    global menu_selection
    global last_menu_selection
    global nextmove
    global nextfruit
    global redraw
    global renderer
    # Game Initialization Block  
    last_status=""
    board.set_lives(3)
    board.set_score(0)
    game_mode=PLAY
    menu_selection=CONTINUE
    last_menu_selection=CONTINUE
    nextmove=pygame.time.get_ticks()+DELAY
    nextfruit=pygame.time.get_ticks()+(DELAY * random.randint(5, 20))
    redraw=1
    board.get_level().create_empty_map()
    
# Game Initialization Block 
init_game()

# main game loop
while game_mode != EXIT:
    last_game_mode=game_mode
    last_menu_selection=menu_selection
    if DEBUG:
        #print "Mode: " + str(game_mode)
        pass
    if game_mode == PLAY:           
        game_event_handler()
        if pygame.time.get_ticks()>nextmove:
            nextmove=pygame.time.get_ticks()+DELAY
            board.add_snake_head()
            board.eat_fruit()
            global nextfruit
            if pygame.time.get_ticks()>nextfruit:
                board.add_fruit()
                nextfruit=pygame.time.get_ticks()+(DELAY * random.randint(5, 20))

        renderer.draw_game_board(board, 1) # this may or may not make sense to be in the if
    elif game_mode == MENU:
        menu_event_handler()
        draw_menu(redraw)

    if last_game_mode != game_mode:
        redraw=1
    else:
        redraw=0  

    FPSCLOCK.tick(FPS)

pygame.quit()
sys.exit()
