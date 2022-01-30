import pygame
from pygame.locals import *
from grid import Grid

pygame.init()
screen_width, screen_height = 750, 750   # Resolution -> 1600, 900
rows = 50
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Shortest Path Finding')

#Algorithm



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
            position_start = pygame.mouse.get_pos()
            grid.grid_update(position_start,'start')
        
        if pygame.mouse.get_pressed()[2]: #right button
            position_goal = pygame.mouse.get_pos()
            grid.grid_update(position_goal,'goal')
        
        if pygame.mouse.get_pressed()[1]: #mid button
            position_barrier = pygame.mouse.get_pos()
            grid.grid_update(position_barrier,'barrier')

        # True when the keyboard give the input
        if event.type == KEYDOWN:
            
            # key define the which input and K
            if event.key == K_RETURN:
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.event.set_blocked(pygame.MOUSEMOTION)
                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                pygame.event.set_blocked(pygame.MOUSEWHEEL)


                grid.searching_algorithms("BFS", position_start, position_goal, grid, win, pygame.display.update)
                

                

  
    pygame.display.update()
    pygame.time.Clock().tick(60)






