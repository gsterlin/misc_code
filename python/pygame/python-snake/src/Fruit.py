import random

class Fruit(object):
    def __init__(self, field):
        self.coordinates = []
        self.field = field
    
    def add_next(self):
        #if dirt.count((x,y)) > 0 or snake.get_body().count((x,y)) > 0 or #fruit.count((x,y)) > 0:
            #add_fruit(tries-1)
        #else:
        self.coordinates.append((random.randint(0, self.field.get_width()), random.randint(0, self.field.get_height())) )
    
    def at_coordinate(self, x, y):
        at_coordinate=0
        if self.fruit.count((x, y)) > 0:
            at_coordinate=1
        return at_coordinate
    
    def remove_coordinate(self, coordinate):
        self.coordinates.remove(coordinate)
        
    def get_coordinates(self):
        return self.coordinates

