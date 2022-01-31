import pygame
from colors import Colors


class Node:

    
    def __init__(self, row, col, width):
        self.neighbours = []

        # position in grid
        self.row = row
        self.col = col

        # initial color
        self.color = Colors.white

        # position in screen
        self.x= row * width
        self.y = col * width
        # height and height of the node
        self.width = width

        # parent of this node
        self.parent  = None


    def get_pos(self):
        return self.row, self.col
    def make_start(self):
        self.color = Colors.red
    def make_goal(self):
        self.color = Colors.blue
    def make_barrier(self):
        self.color = Colors.black
    def make_open(self):
        self.color = Colors.gold
    def make_closed(self):
        self.color = Colors.aqua
    def make_path(self):
        self.color = Colors.teal
    def is_start(self):
        return self.color == Colors.red
    def is_goal(self):
        return self.color == Colors.blue
    def is_barrier(self):
        return self.color == Colors.black
    def is_open(self):
        return self.color == Colors.gold
    def is_closed(self):
        return self.color == Colors.aqua
    def reset(self):
        self.color = Colors.white
        self.parent = None
    def draw_node(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width,self.width))

        #for black borders around the Node
        pygame.draw.rect(win, Colors.black, (self.x, self.y, self.width, self.width),1)
    
    def set_parent(self, node):
        self.parent = node

    def get_parent(self):
        return self.parent



    # (5, 5) -> {'right' : (5,6), "left": (5,4), "up" : (4,5),"down" : (6,5)} ]
    def has_neighbours(self,grid, rows):
        # down
        if self.row + 1>=0 and (self.row + 1)<rows and not (grid[self.row+1][self.col].is_barrier()):
            self.neighbours.append(grid[self.row+1][self.col])
        # up
        if self.row  -1>=0 and (self.row  -1)<rows and not (grid[self.row-1][self.col].is_barrier()):
            self.neighbours.append( grid[self.row-1][self.col] ) 
        #right
        if self.col + 1>=0 and (self.col + 1)<rows and not (grid[self.row][self.col + 1].is_barrier()):
            self.neighbours.append(grid[self.row][self.col + 1])
        #left
        if self.col - 1>=0 and (self.col - 1)<rows and not (grid[self.row][self.col-1].is_barrier()):
            self.neighbours.append(grid[self.row][self.col-1])
        
        return self.neighbours

    def __eq__(self, node) -> bool:
        return self.get_pos() == node.get_pos()

    # for handling the error of the Priority Comparision in priority Queue
    def __lt__(self, other):
        return False
        






    
    
    



