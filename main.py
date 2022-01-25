from cProfile import run
from tracemalloc import start
import pygame
from pygame.locals import *
from colors import colors
from grid import Grid
from queue import PriorityQueue

pygame.init()
screen_width, screen_height = 750, 750   # Resolution -> 1600, 900
rows = 50
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Shortest Path Finding')


#main
grid = Grid(rows, screen_width)
grid.make_grid()


run = True


while run:
    # draw the grid
    grid.draw_grid(win)
    

    # for all events in screen
    for event in pygame.event.get():
        if event.type == QUIT:
                run = False
        if pygame.mouse.get_pressed()[0]: #left button
            position = pygame.mouse.get_pos()
            grid.grid_update(position,'start')
        
        if pygame.mouse.get_pressed()[2]: #left button
            position = pygame.mouse.get_pos()
            grid.grid_update(position,'goal')
        
        if pygame.mouse.get_pressed()[1]: #left button
            position = pygame.mouse.get_pos()
            grid.grid_update(position,'barrier')

        # True when the keyboard give the input
        if event.type == KEYDOWN:
            # key define the which input.
            if event.key == K_KP_ENTER:
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.event.set_blocked(pygame.MOUSEMOTION)
                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                pygame.event.set_blocked(pygame.MOUSEWHEEL)
        
        

        






    



    pygame.display.update()
    pygame.time.Clock().tick(60)

    def Algorithm(Grid, Start, Goal):
        frontier  = PriorityQueue()
        frontier.put((2,Start))
        
        if frontier.empty():
            return "not found"
        else:
            if frontier.get()[1] == Goal:
                return frontier.get()[1]
            else:
                pass



