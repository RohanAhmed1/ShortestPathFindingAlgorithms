import pygame
from colors import colors


class Node:

    
    def __init__(self, row, col, width):
        self.neighbours = []
        self.row = row
        self.col = col
        self.width = width
        self.color = colors.white
        # in pygame screen
        self.x= row * width
        self.y = col * width
        self.parent  = None


    def get_pos(self):
        return self.row, self.col
    def make_start(self):
        self.color = colors.red
    def make_goal(self):
        self.color = colors.blue
    def make_barrier(self):
        self.color = colors.black
    def make_open(self):
        self.color = colors.gold
    def make_closed(self):
        self.color = colors.aqua
    def make_path(self):
        self.color = colors.teal
    def is_start(self):
        return self.color == colors.red
    def is_goal(self):
        return self.color == colors.blue
    def is_barrier(self):
        return self.color == colors.black
    def is_open(self):
        return self.color == colors.gold
    def is_closed(self):
        return self.color == colors.aqua
    def reset(self):
        self.color = colors.white
        self.parent = None
    def draw_node(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width,self.width))

        #for black borders around the Node
        pygame.draw.rect(win, colors.black, (self.x, self.y, self.width, self.width),1)
    
    def set_parent(self, node):
        self.parent = node

    def get_parent(self):
        return self.parent


        

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

    def __lt__(self, other):
        return False
        






    
    
    



