# http://rene.f0o.com/mywiki/PythonGameProgramming
# http://inventwithpython.com/makinggames.pdf

import pygame, sys, os, random
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

from ImageBall import ImageBall
from VectorBall import VectorBall
from PyGameBall import PyGameBall
from Ball import Ball

# Constants
FPS = 30
BLACK = (0, 0, 0)

screenX = 800
screenY = 480

debug = 0
Ball.setDebug(debug)

fpsClock = pygame.time.Clock()

pygame.init()
displaySurface = pygame.display.set_mode((screenX, screenY))
pygame.display.set_caption('Simple Bouncing Ball')
screen = pygame.display.get_surface()

tile = pygame.image.load('background.png')

PyGameBall.loadSounds()

## Background Music
pygame.mixer.music.load('tetrisc.mid')
pygame.mixer.music.play(-1, 0.0)

## Initial Settings
musicPlaying = True
trails = False

balls = []
ballMode = 'vector'

while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            print event.button
            ball = None
            if ballMode == 'vector':
                color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
                ball = VectorBall(screen, color, 14, 1, 0)
            if ballMode == 'image':
                ball = ImageBall(screen, "BlueBall.png", 1, 1)
            ball.setPosition(event.pos[0], event.pos[1])
            balls.append(ball)
        elif event.type == MOUSEMOTION:
            pass
        else: 
            print event
        
        if event.type == KEYUP:
            # allow ESC to close game
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == ord('a'):
                Ball.switchAirResistance()
            if event.key == ord('g'):
                Ball.switchGravity()
            # Stop / start the background mucis    
            if event.key == ord('m'):
                if musicPlaying:
                    pygame.mixer.music.stop()
                    musicPlaying = False
                else:
                    pygame.mixer.music.play(-1, 0.0)
                    musicPlaying = True
            
            if event.key == ord('t'):
                if trails:
                    trails = False
                else:
                    trails = True
                    
            if event.key == ord('c'):
                if balls:
                    print "Ball Count:", Ball.getInstanceCount()
                    print "Ball Bounce Count:", Ball.getInstanceBounceCount()
                else:
                    print "Ball Count: 0"
                    print "Ball Bounce Count: 0"
         
            if event.key == ord('i'):
                ballMode = 'image'
                print "Setting ball mode to image"
         
            if event.key == ord('v'):
                ballMode = 'vector'
                print "Setting ball mode to vector"
            
            if event.key == ord('d'):
                if debug:
                    print "Disabling Debug"
                    debug = 0
                else:
                    print "Enabling Debug"
                    debug = 1
                Ball.setDebug(debug)
                    
    pygame.display.update()

    # This here clears out the screen to remove trails
    if trails == False:
        #pygame.draw.rect(screen, BLACK, (0, 0, screenX, screenY))
        for x in range(50):
            for y in range(30):
                screen.blit(tile, (x * 16, y * 16))
    

    for ball in balls:
        ball.move()
    
    pygame.display.flip()
    
    fpsClock.tick(FPS)
    