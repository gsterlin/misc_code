class Field(object):
    def __init__(self, width=10, height=10):
        self.height = height
        self.width = width
        
    def get_width(self):
        return self.width
    
    def get_height(self):
        return self.height
    
    def get_adjusted_coordinate(self, x, y):
        if x > self.get_width():
            x = 0
        elif x < 0:
            x = self.get_width()
        if y > self.get_height():
            y = 0
        elif y < 0:
            y = self.get_height()
        
        return (x, y)
    
    
