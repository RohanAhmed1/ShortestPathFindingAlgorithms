# built-in Queues
from queue import Queue, PriorityQueue, LifoQueue
from time import sleep

# common method for all Algorithms
class DrawUpdate:

    def draw_goal_path(self,node, grid_win, win, pygame):
        while node.get_parent() is not None:
            node.make_path()
            #update the screen
            grid_win.draw_grid(win)
            sleep(0.02)
            pygame()

            #for getting next node
            node = node.get_parent()


class BFS(DrawUpdate):

    def BFS_algorithm(self, grid, start, goal, rows, grid_win, win, pygame):
        # algorithm
        open_set = PriorityQueue()
        heur = self.cal_heuristic(start, goal)
        open_set.put([heur, start])
        closed_set = []


        while open_set is not open_set.empty():
            item = open_set.get()
            # item[1] is the node and item[0] is the heuristic of that node
            node = item[1]
            if node in closed_set:
                continue
            if node == goal:
                self.draw_goal_path(node, grid_win, win, pygame)

                # for making start and goal node coloures again
                start.make_start()
                goal.make_goal()

                # update the screen
                grid_win.draw_grid(win)
                sleep(0.01)
                pygame()

                # algirthm complete
                return
        
            closed_set.append(node)
            
            node.make_closed()

            #update the screen
            grid_win.draw_grid(win)
            sleep(0.02)
            pygame()

            
            for each in node.has_neighbours(grid, rows):
                heur = self.cal_heuristic(each, goal)
                open_set.put([heur, each])
                if not each.is_closed():
                    each.set_parent(node)
                    each.make_open()

                    #update the screen
                    grid_win.draw_grid(win)
                    sleep(0.01)
                    pygame()

        



            
        
            


        return "not found"
        
    # distance between two points
    def cal_heuristic(self, start, goal):
        start_row, start_col = start.get_pos()
        goal_row, goal_col = goal.get_pos()

        return abs(goal_row - start_row) + abs(goal_col - start_col)







class BrFS(DrawUpdate):

    def BrFS_algorithm(self, grid, start, goal, rows, grid_win, win, pygame):
        # algorithm
        open_set = Queue()
        open_set.put([start])
        closed_set = []


        while open_set is not open_set.empty():
            item = open_set.get()
            # item[1] is the node and item[0] is the heuristic of that node
            node = item[0]
            if node in closed_set:
                continue
            if node == goal:
                self.draw_goal_path(node, grid_win, win, pygame)
                # for making start and goal coloured again
                start.make_start()
                goal.make_goal()

                # update the screen
                grid_win.draw_grid(win)
                sleep(0.01)
                pygame()
                return
            closed_set.append(node)
            
            node.make_closed()

            #update the screen
            grid_win.draw_grid(win)
            sleep(0.02)
            pygame()

            
            for each in node.has_neighbours(grid, rows):
                open_set.put([each])
                if not each.is_closed():
                    each.set_parent(node)
                    each.make_open()

                    #update the screen
                    grid_win.draw_grid(win)
                    sleep(0.01)
                    pygame()

        
        








class DFS(DrawUpdate):

    def DFS_algorithm(self, grid, start, goal, rows, grid_win, win, pygame):
        # algorithm
        open_set = LifoQueue()
        open_set.put([start])
        closed_set = []


        while open_set is not open_set.empty():
            item = open_set.get()
            # item[1] is the node and item[0] is the heuristic of that node
            node = item[0]
            if node in closed_set:
                continue
            if node == goal:
                self.draw_goal_path(node, grid_win, win, pygame)
                # for making start and goal coloured again
                start.make_start()
                goal.make_goal()

                # update the screen
                grid_win.draw_grid(win)
                sleep(0.01)
                pygame()
                return
                return
            closed_set.append(node)
            
            node.make_closed()
            grid_win.draw_grid(win)
            sleep(0.02)
            pygame()

            
            for each in node.has_neighbours(grid, rows):
                open_set.put([each])
                if not each.is_closed():
                    each.set_parent(node)
                    each.make_open()

                    # update the screen
                    grid_win.draw_grid(win)
                    sleep(0.01)
                    pygame()

        