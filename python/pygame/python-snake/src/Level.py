class Level(object):
    def __init__(self):
        self.dirt=[]
        
    def create_empty_map(self):
        self.dirt=[]

    def create_bounds_map(self):
        self.dirt=[]
        for x in range(0,40):
            self.dirt.append((x, 0))
            self.dirt.append((x,22))
        for y in range(1,22):
            self.dirt.append((0, y))
            self.dirt.append((39, y))
            
    def get_dirt(self):
        return self.dirt
