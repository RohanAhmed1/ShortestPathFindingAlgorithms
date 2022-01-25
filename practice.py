
from cProfile import run
import pygame
from pygame.locals import *
from colors import colors
from grid import Grid

pygame.init()
screen_width, screen_height = 900, 500   # Resolution -> 1600, 900
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
            grid.grid_update(position)
        
        if pygame.mouse.get_pressed()[2]: #right button
            position = pygame.mouse.get_pos()
            pygame.draw.rect(win, colors.black, (position[0]*,position[1]*,50,50))
            
            

        
        
        







    



    pygame.display.update()
    pygame.time.Clock().tick(60)