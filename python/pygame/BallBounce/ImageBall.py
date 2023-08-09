import pygame

from PyGameBall import PyGameBall

class ImageBall(PyGameBall):
    
    def __init__(self, screen, imageFile, velocityX, velocityY):
        '''ImageBall Constructor'''
        self.image = pygame.image.load(imageFile)
        self.image = pygame.transform.scale2x(self.image)
        self.image = pygame.transform.scale2x(self.image)
        width = self.image.get_width()
        height = self.image.get_height()
        super(ImageBall, self).__init__(screen, width, height, velocityX, velocityY)
        
    def draw(self):
        self.screen.blit(self.image, self.getPosition())


