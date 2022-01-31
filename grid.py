
from node import Node
from Algorithms import BFS, DFS, BrFS


class Grid:
    # take those inputs in __init__  which are must to create object
    def __init__(self, rows, width):
        self.grid = []
        self.rows = rows
        self.width = width

        # set start_node and goal_node
        self.start_node = False
        self.goal_node = False


    
    def make_grid(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.rows):
                node = Node(i, j, (self.gap_between(self.rows, self.width)))
                self.grid[i].append(node)

    def draw_grid(self, win):
        for i in range(self.rows):
            for j in range(self.rows):
                node = self.grid[i][j]
                node.draw_node(win)

    
    
    
    def grid_update(self, position, do):

        #position in grid
        row= position[0] // self.gap_between(self.rows, self.width)
        col= position[1] // self.gap_between(self.rows, self.width)

        # node in grid
        node  = self.grid[row][col]
 
        if not(node.is_start()) and not self.start_node and do =="start":    
            node.make_start()
            self.start_node = node
        if not(node.is_goal()) and not self.goal_node and do =="goal":
            node.make_goal()
            self.goal_node = node
        if not(node.is_barrier()) and not(node.is_start()) and not(node.is_goal()) and do =="barrier":
            node.make_barrier()
        




    # for calculating how many columns in the screen width or rows in the height
    def gap_between(self, rows, width):
        return width // rows  


    def searching_algorithms(self, algorithm, start, goal, grid, win, pygame):
        #for pixels value into the Grid location

        # node in grid
        start  = self.grid[start.get_pos()[0]][start.get_pos()[1]]
        goal  = self.grid[goal.get_pos()[0]][goal.get_pos()[1]]

        # choose algorithm
        if algorithm == "BFS":
            bfs = BFS()
            bfs.BFS_algorithm(self.grid, start, goal, self.rows, grid, win, pygame)
        elif algorithm == "DFS":
            bfs = DFS()
            bfs.DFS_algorithm(self.grid, start, goal, self.rows, grid, win, pygame)
        elif algorithm == "BrFS":
            bfs = BrFS()
            bfs.BrFS_algorithm(self.grid, start, goal, self.rows, grid, win, pygame)




