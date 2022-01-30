from time import sleep
from queue import PriorityQueue
class BFS:
    goal_node = None

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
                return
            closed_set.append(node)
            
            node.make_closed()
            grid_win.draw_grid(win)
            sleep(0.02)
            pygame()

            
            for each in node.has_neighbours(grid, rows):
                heur = self.cal_heuristic(each, goal)
                open_set.put([heur, each])
                if not each.is_closed():
                    each.set_parent(node)
                    each.make_open()
                    grid_win.draw_grid(win)
                    sleep(0.01)
                    pygame()



            
        
            


        return "not found"
        

    def cal_heuristic(self, start, goal):
        start_row, start_col = start.get_pos()
        goal_row, goal_col = goal.get_pos()

        return abs(goal_row - start_row) + abs(goal_col - start_col)

    def draw_goal_path(self,node, grid_win,win, pygame):
        while node.get_parent() is not None and node.is_closed:
            node.make_path()
            #update the screen
            grid_win.draw_grid(win)
            sleep(0.02)
            pygame()

            #for getting next node
            node = node.get_parent()





