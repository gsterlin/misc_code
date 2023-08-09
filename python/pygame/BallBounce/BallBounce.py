# http://rene.f0o.com/mywiki/PythonGameProgramming
# http://inventwithpython.com/makinggames.pdf

import pygame, sys, os
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

surface_x = 800
surface_y = 480

block_width_x = 14
block_width_y = 14

block_velocity_x = 1
block_velocity_y = 1

block_position_x = 10
block_position_y = 10

test_file_name = os.path.join("test.png")

pygame.init()
DISPLAYSURF = pygame.display.set_mode((surface_x, surface_y))
pygame.display.set_caption('Simple Bouncing Ball')
screen = pygame.display.get_surface() 
print test_file_name

test_surface = pygame.image.load(test_file_name)

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        else: 
            print event 
    pygame.display.update()
    
    if block_position_x + block_velocity_x < 0:
        block_velocity_x *= -1
    if block_position_x + block_width_x + block_velocity_x > surface_x:
        block_velocity_x *= -1
    if block_position_y + block_velocity_y < 0:
        block_velocity_y *= -1
    if block_position_y + block_width_y + block_velocity_y > surface_y:
        block_velocity_y *= -1
        
    block_position_x += block_velocity_x
    block_position_y += block_velocity_y
    
    screen.blit(test_surface, (block_position_x,block_position_y)) 
    pygame.display.flip() 