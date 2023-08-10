from Snake import Snake
from Fruit import Fruit
from Level import Level
from Field import Field
from Direction import Direction

class Board(object):
    def __init__(self, field):
        self.field = field
        self.snake = Snake(field)
        self.snake.set_direction(Direction.get_north())
        self.snake.set_last_direction(self.snake.get_direction())

        self.removed=[]
        self.fruit = Fruit(field)
        self.level = Level()
        self.lives = 0
        self.score = 0

    def get_field(self):
        return self.field
    
    def get_snake(self):
        return self.snake
    
    def get_removed(self):
        return self.removed
    
    def get_fruit(self):
        return self.fruit
    
    def get_level(self):
        return self.level

    def get_lives(self):
        return self.lives
    
    def set_lives(self, lives):
        self.lives = lives
        
    def get_score(self):
        return self.score
    
    def set_score(self, score):
        self.score = score
    
    
    
    def add_snake_head(self):
        snake = self.get_snake()
        lives = self.get_lives()

        snake.add_next_head()
    
        if snake.ate_self() or self.hit_dirt():
            self.set_lives(lives - 1)
            if lives == 0:
                game_mode=MENU
            else:
                global redraw
                redraw = 1
                self.fruit = Fruit(self.field)
                self.snake = Snake(self.field)
                self.snake.set_direction(Direction.get_north())
                self.snake.set_last_direction(self.snake.get_direction())



    def eat_fruit(self):
        score = self.get_score()
        snake = self.get_snake()
        fruit = self.get_fruit()
        head=snake.get_head()
        if fruit.get_coordinates().count(head) > 0:
            # check for fruit value to give points
            snake.inc_max_size()
            self.set_score(score + 10)
            fruit.remove_coordinate(head)
            
    def hit_dirt(self):
        hit=0
        if self.get_level().get_dirt().count(self.get_snake().get_head()) > 0:
            hit=1
        return hit
            
    def add_fruit(self, tries=10):
        self.get_fruit().add_next()