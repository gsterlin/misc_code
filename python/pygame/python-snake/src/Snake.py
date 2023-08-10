from Direction import Direction

class Snake(object):
    def __init__(self, field, start_pos=(10, 10), max_size=5, last_direction=Direction.get_neutral(), direction=Direction.get_neutral()):
        self.max_size = max_size
        self.body = [start_pos]
        self.removed = []
        self.last_direction = last_direction
        self.direction = direction
        self.field = field

    def get_last_direction(self):
        return self.last_direction
    
    def set_last_direction(self, direction):
        self.last_direction = direction
        
    def get_direction(self):
        return self.direction
    
    def set_direction(self, direction):
        self.direction = direction
        
    def set_max_size(self, max_size):
        self.max_size = max_size
        
    def inc_max_size(self, amount=1):
        self.max_size += amount
        
    def dec_max_size(self, amount=1):
        self.max_size -= amount
        
    def get_max_size(self):
        return self.max_size
    
    def get_size(self):
        return len(self.body)
    
    def get_removed(self):
        return self.removed
    
    def add_removed(self, removed):
        self.removed.append(removed)
        
    def clear_removed(self):
        self.removed = []
    
    def get_head(self):
        return self.body[0]

    def add_head(self, x, y):
        x, y = self.field.get_adjusted_coordinate(x, y)
        self.body.insert(0, (x, y))
        self.set_last_direction(self.get_direction())
        if self.get_size() > self.get_max_size():
            self.remove_tail()
    
    def add_head_direction(self, direction):
        x, y = self.get_head()
        self.set_direction(direction)
        x, y = Direction.get_next_coordinates(x, y, self.get_direction())
        self.add_head(x, y)
        
    def add_next_head(self):
        self.add_head_direction(self.get_direction())
        
    def remove_tail(self):
        self.add_removed(self.body.pop())
        
    def get_body(self):
        return self.body
    
    def ate_self(self):
        head = self.get_head()
        body = self.get_body()
        return body.count(head) - 1
