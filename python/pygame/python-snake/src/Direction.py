class Direction(object):
    
    # Class Variables
    NEUTRAL = 0
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4
    
    @classmethod
    def get_north(cls):
        return cls.NORTH
    
    @classmethod
    def get_east(cls):
        return cls.EAST
    
    @classmethod
    def get_south(cls):
        return cls.SOUTH
    
    @classmethod
    def get_west(cls):
        return cls.WEST
    
    @classmethod
    def get_neutral(cls):
        return cls.NEUTRAL
    
    @classmethod
    def get_next_coordinates(cls, x, y, direction):
        if direction==Direction.get_north():
            y=y-1
        elif direction==Direction.get_south():
            y=y+1
        elif direction==Direction.get_west():
            x=x-1
        elif direction==Direction.get_east():
            x=x+1
        return x, y
