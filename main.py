import pygame
from pygame.locals import *
from grid import Grid


# initialize the pygame and set screen 
pygame.init()
screen_width, screen_height = 750, 750   # Resolution -> 1600, 900
win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Path Finding Algorithms Visualizer')


#main

# rows and column in screen 
rows = 50

# grid
grid = Grid(rows, screen_width)
grid.make_grid()

# screen in loop
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

        
        #only allowed keyboards when the start and goal node defined
        if grid.start_node and grid.goal_node:


        # True when the keyboard give the input
            if event.type == KEYDOWN:

                # after setting the goal , barriers, and start, mouse inputs blocked
                pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                pygame.event.set_blocked(pygame.MOUSEMOTION)
                pygame.event.set_blocked(pygame.MOUSEBUTTONUP)
                pygame.event.set_blocked(pygame.MOUSEWHEEL)

                
                # key define the which input of keyboard
                if event.key == K_b:  # B button
                    grid.searching_algorithms("BFS", grid.start_node, grid.goal_node, grid, win, pygame.display.update)
                elif event.key == K_d: # D button
                    grid.searching_algorithms("DFS", grid.start_node, grid.goal_node, grid, win, pygame.display.update)
                elif event.key == K_r: # R button
                    grid.searching_algorithms("BrFS", grid.start_node, grid.goal_node, grid, win, pygame.display.update)


                # for resetting the game
                elif event.key == K_RETURN:   # K_RETURN is for the enter button in the keyboard

                    # make grid again, all values will be reset
                    grid = Grid(rows, screen_width)
                    grid.make_grid()

                    #it allowed all the events ( also those events which are blocked )
                    pygame.event.set_allowed(None)

                

    # for updating the screen 
    pygame.display.update()
    pygame.time.Clock().tick(60)



# exit from the pygame
pygame.quit()








