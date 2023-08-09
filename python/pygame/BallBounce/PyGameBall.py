from Ball import Ball

import pygame

class PyGameBall(Ball):
    '''This class manages all of the 'interesting' things for drawing a Ball to a screen'''
    # Make sounds a class variable to conserve memory.  Otherwise memory consumption was going up rapidly!
    sounds = {}
    
    def __init__(self, screen, width, height, velocityX, velocityY):
        areaWidth = screen.get_width()
        areaHeight = screen.get_height()
        super(PyGameBall, self).__init__(width, height, velocityX, velocityY, areaWidth, areaHeight)
        self.screen = screen
        #self.sounds = self.loadSounds()

    @classmethod
    # Appears that this cannot be called until after the pygame.init has occured
    def loadSounds(cls):
        '''Load Sounds necessary for the PyGameBall class and children.'''
        cls.sounds['bounce'] = pygame.mixer.Sound('blip.wav')
    
    def playSound(self, sound, velocity):
        '''Play Ball sound'''
        if (sound in PyGameBall.sounds):
            volume = float(abs(velocity))/40
            channel = pygame.mixer.find_channel(True)
            channel.set_volume(volume)
            channel.play(PyGameBall.sounds[sound])
            if Ball.debug:
                print "Playing Sound: " + sound + " Volume: " + str(volume)
        else:
            raise Exception('Undefined sound type:', sound)

    def move(self):
        isBounceX = self.isBounceX()
        isBounceY = self.isBounceY()
        if isBounceX and isBounceY:
            self.playSound('bounce', self.velocityX + self.velocityY)
        elif isBounceX:
            self.playSound('bounce', self.velocityX)
        elif isBounceY:
            self.playSound('bounce', self.velocityY)
        super(PyGameBall, self).move()
        self.draw()
        
    def draw(self):
        raise Exception("draw method not implemented")
        