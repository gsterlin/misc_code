#from pygame.locals import *

import math

class Renderer(object):

    # Class Variables
    WINDOWX = 800            # size of window's width in pixels
    WINDOWY = 480            # size of windows' height in pixels

    # Shapes
    SQUARE=0
    CIRCLE=1
    
    # Segments
    SEGSIZE = 20
    HEADER=SEGSIZE           # The size of the score/info banner in pixels
    HEADERFONTSIZE=HEADER-2  # The size of the font for score/info banner in pixels
    FONT='freesansbold.ttf'  # The name of the font to use for the header
    fontObj = None
    #SEGX=(renderer.get_width()/SEGSIZE)-1 # The number of segments wide supported
    #SEGY=(renderer.get_height()/SEGSIZE)-2 # The number of segments high supported

    
    # Color Constants
    BLUE = (0, 0, 128)       # color code for blue we want to use
    GREEN = (0, 255, 0)      # color code for green we want to use
    RED = (255, 0, 0)        # color code for red we want to use
    BLACK = (5, 5, 5)        # color code for black we want to use
    WHITE = (255, 255, 255)  # color code for white we want to use
    BROWN = (86, 56, 0)      # color code for brown we want to use

    DARK_GREEN = (0, 128, 0) 
    
    def __init__(self, pygame):
        Renderer.set_pygame(pygame)
        Renderer.fontObj = pygame.font.Font(Renderer.FONT, Renderer.HEADERFONTSIZE)

    @classmethod
    def get_pygame(cls):
        return cls.pygame

    @classmethod
    def set_pygame(cls, pygame, fullscreen=0, doublebuffer=0, hwsurface=0):
        display_options=0
        if fullscreen:
            display_options=display_options|pygame.FULLSCREEN
        if doublebuffer:
            display_options=display_options|pygame.DOUBLEBUF
        if hwsurface:
            display_options=display_options|pygame.HWSURFACE
        cls.pygame = pygame
        cls.DISPLAYSURF = cls.pygame.display.set_mode((cls.get_width(), cls.get_height()), display_options)
        
    @classmethod
    def get_width(cls):
        return cls.WINDOWX
        
    @classmethod
    def get_height(cls):
        return cls.WINDOWY
        
    @classmethod    
    def draw_board_segment(cls, x, y, color, shape=SQUARE):
        rect=()
        if shape==cls.SQUARE:
            x_pos=(x*cls.SEGSIZE)
            y_pos=(y*cls.SEGSIZE) + cls.HEADER
            rect=cls.pygame.draw.rect(cls.DISPLAYSURF, color, (x_pos, y_pos, cls.SEGSIZE, cls.SEGSIZE), 0)
        elif shape==cls.CIRCLE:
            x_pos=(x*cls.SEGSIZE) + (cls.SEGSIZE/2)
            y_pos=(y*cls.SEGSIZE) + (cls.SEGSIZE/2) + cls.HEADER
            radius=cls.SEGSIZE/2
            rect=cls.pygame.draw.circle(cls.DISPLAYSURF, color, (x_pos, y_pos), radius, 0)
        return rect
        
    @classmethod    
    def clear_board_segment(cls, x, y):
        return cls.draw_board_segment(x, y, cls.BLACK)
        
    @classmethod    
    def draw_snake_segment(cls, x, y):
        return cls.draw_board_segment(x, y, cls.GREEN)

    @classmethod    
    def draw_fruit_segment(cls, x, y):
        return cls.draw_board_segment(x, y, cls.RED, cls.CIRCLE)

    @classmethod    
    def draw_dirt_segment(cls, x, y):
        return cls.draw_board_segment(x, y, cls.BROWN)
    
    @classmethod    
    def draw_text_line(cls, text="", color=BLACK, background=WHITE, position=(0,0)):
        rect=cls.pygame.draw.rect(cls.DISPLAYSURF, background, (position[0], position[1], cls.get_width(), cls.HEADER))
        textSurfaceObj = cls.fontObj.render(text, True, color, background)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.topleft=position
        cls.DISPLAYSURF.blit(textSurfaceObj, textRectObj)
        return rect

    @classmethod    
    def draw_game_header(cls, board, redraw=0):
        #global last_status
        todo=[]
        #status='Score:' + str(board.get_score()) + ' Size:' + str(board.get_snake().get_max_size()) + ' Lives:' + str(board.get_lives()) + ' FPS:' + str(math.floor(FPSCLOCK.get_fps()))
        status='Score:' + str(board.get_score()) + ' Size:' + str(board.get_snake().get_max_size()) + ' Lives:' + str(board.get_lives())
        print status

        if redraw:
            last_status=status
            todo.append(cls.draw_text_line(status, color=cls.GREEN, background=cls.BLUE))   
        return todo
 
    @classmethod    
    def draw_snake(cls, snake, redraw=0):
        todo=[]
        if redraw:
            for segment in snake.get_body():
                todo.append(cls.draw_snake_segment(segment[0], segment[1]))
        else:
            x, y=snake.get_head()
            todo.append(cls.draw_snake_segment(x, y))
        return todo

    @classmethod    
    def draw_fruit(cls, fruit, redraw=0):
        todo=[]
        if redraw:
            for item in fruit.get_coordinates():
                todo.append(cls.draw_fruit_segment(item[0], item[1]))
        else:
            if len(fruit.get_coordinates()) > 0:
                todo.append(cls.draw_fruit_segment(fruit.get_coordinates()[-1][0], fruit.get_coordinates()[-1][1]))
        return todo        

    @classmethod
    def draw_dirt(cls, level, redraw=0):
        todo=[]
        for segment in level.get_dirt():
            todo.append(cls.draw_dirt_segment(segment[0], segment[1]))
        return todo

    @classmethod    
    def clear_removed(cls, snake, redraw=0):
        todo=[]
        removed = snake.get_removed()
        if not redraw and removed != None:
            for segment in snake.get_removed():
                todo.append(cls.clear_board_segment(segment[0], segment[1]))
        snake.clear_removed()
        return todo

    @classmethod    
    def clear_screen(cls, color=BLACK):
        return cls.pygame.draw.rect(cls.DISPLAYSURF, color, (0, 0, cls.get_width(), cls.get_height()))    

    @classmethod    
    def draw_game_board(cls, board, redraw=1):
        global removed
        global last_status
        todo=[]
        if redraw:
            print "Redrawing!!!!!"
            todo.append(cls.clear_screen())
        todo.extend(cls.draw_snake(board.get_snake(), redraw))
        todo.extend(cls.clear_removed(board.get_snake(), redraw))
        todo.extend(cls.draw_fruit(board.get_fruit(), redraw))
        todo.extend(cls.draw_dirt(board.get_level(), redraw))
        todo.extend(cls.draw_game_header(board, redraw))
        cls.pygame.display.update(todo)
 
    @classmethod    
    def draw_menu(cls, redraw=0):
        global menu_selection
        global last_menu_selection
        todo=[]
        continue_background=cls.BLUE
        newgame_background=cls.BLUE
        endgame_background=cls.BLUE
        if menu_selection==CONTINUE:
            continue_background=cls.RED
        elif menu_selection==NEWGAME:
            newgame_background=cls.RED
        elif menu_selection==ENDGAME:
            endgame_background=cls.RED
        todo.append(DISPLAYSURF.fill(cls.BLACK))
        todo.append(draw_text_line(text="Continue", color=cls.GREEN, background=continue_background, position=(0,0)))
        todo.append(draw_text_line(text="New Game", color=cls.GREEN, background=newgame_background, position=(0,20)))
        todo.append(draw_text_line(text="End Game", color=cls.GREEN, background=endgame_background, position=(0,40)))
        self.pygame.display.update(todo)

