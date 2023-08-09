import pygame

from PyGameBall import PyGameBall

class VectorBall(PyGameBall):
    
    def __init__(self, screen, color, size, velocityX, velocityY):
        '''VectorBall Constructor'''
        super(VectorBall, self).__init__(screen, size, size, velocityX, velocityY)
        self.color = color
        
    def draw(self):
        pygame.draw.ellipse(self.screen, self.color, self.getRect(), 0)
        
