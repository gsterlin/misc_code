class Ball(object):
    '''Ball Class that does fancy ball bouncing stuff'''
    # Class variables
    instanceCounter = 0
    instanceBounceCounter = 0
    hasGravity = False
    hasAirResistance = False
    debug = 0
    
    def __init__(self, width, height, velocityX, velocityY, areaWidth, areaHeight):
        '''Ball Constructor'''
        self.width = width
        self.height = height
        self.velocityX = velocityX
        self.directionX = 1
        self.velocityY = velocityY
        self.directionY = 1
        self.areaWidth = areaWidth
        self.areaHeight = areaHeight      
        self.positionX = 0
        self.positionY = 0      
        Ball.instanceCounter += 1
        self.mass = 1
        self.global_mass = 1000000000000000
        
    def __del__(self):
        '''Ball Destructor'''
        Ball.instanceCounter -= 1

    @classmethod
    def setDebug(cls, debug):
        '''Set debug on/off'''
        cls.debug = debug
        
    @classmethod    
    def getInstanceCount(cls):
        '''Get the number of instances of the Ball Class'''
        return cls.instanceCounter
    
    @classmethod
    def getInstanceBounceCount(cls):
        '''Get the number of Bounces for all Ball Instances'''
        return cls.instanceBounceCounter

    @classmethod
    def switchGravity(cls):
        if cls.hasGravity == True:
            cls.hasGravity = False
        else:
            cls.hasGravity = True
        
    @classmethod
    def switchAirResistance(cls):
        if cls.hasAirResistance == True:
            cls.hasAirResistance = False
        else:
            cls.hasAirResistance = True

    def getRect(self):
        return self.positionX, self.positionY, self.width, self.height

    def getPosition(self):
        return self.positionX, self.positionY

    def setPosition(self, x, y):
        '''Set the Position of the Ball'''
        # Make sure the ball can't move outside the surface
        # Consider throwing an exception here
        if x + self.width > self.areaWidth:
            self.positionX = self.areaWidth - self.width
        else:
            self.positionX = x
        if y + self.height > self.areaHeight:
            self.positionY = self.areaHeight - self.height
        else:
            self.positionY = y

    def setVelocity(self, velocityX, velocityY):
        if velocityX > 0:
            self.velocityX = velocityX
        else:
            self.velocityX = 0
            self.directionX *= -1
        if velocityY < 0.5 and (self.height + self.positionY) >= self.areaHeight:
            self.velocityY = 0
        elif velocityY > 0:
            self.velocityY = velocityY
        else:
            self.velocityY = 0
            self.directionY *= -1

    def isBounceX(self):
        bounceX = False
        potentialX = self.positionX + self.velocityX
        if potentialX < 0 or potentialX + self.width > self.areaWidth:
            bounceX = True
        return bounceX
    
    def isBounceY(self):
        bounceY = False
        potentialY = self.positionY + self.velocityY
        if potentialY < 0 or potentialY + self.height > self.areaHeight:
            bounceY = True
        return bounceY
    
    def move(self):
        '''Move the Ball Object'''
        isBounceX = self.isBounceX()
        isBounceY = self.isBounceY()
        if isBounceX or isBounceY:
            Ball.instanceBounceCounter += 1
        if isBounceX:
            self.directionX *= -1
        if isBounceY:
            self.directionY *= -1
        if Ball.hasGravity:
            self.applyGravity()
        if Ball.hasAirResistance:
            self.applyAirResistance()
        self.setPosition(self.positionX + (self.velocityX * self.directionX),
                         self.positionY + (self.velocityY * self.directionY))
        if Ball.debug:
            print self.velocityX, self.velocityY, self.directionX, self.directionY
        
    def applyGravity(self):
        gravity = (6.67 * .00000000001 * self.mass * self.global_mass)/((self.positionY+(self.height/2)) * (self.positionY+(self.height/2)))
        if self.velocityY == 0:
            self.directionY = 1
        self.setVelocity(self.velocityX, self.velocityY + (self.directionY * gravity))

    def applyAirResistance(self):
        resistance = 0.01
        self.setVelocity(self.velocityX - (self.velocityX * resistance), self.velocityY - (self.velocityY * resistance))
