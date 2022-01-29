
from node import Node
from Algorithms import BFS


class Grid:
    def __init__(self, rows, width):
        self.grid = []
        self.rows = rows
        self.width = width

        #its for the not making start and goal node again
        self.start  = False
        self.goal = False

    
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
        row= position[0] // self.gap_between(self.rows, self.width)
        col= position[1] // self.gap_between(self.rows, self.width)
        node  = self.grid[row][col]
 
        if not(node.is_start()) and not self.start and do =="start":        
            self.grid[row][col].make_start()
            self.start = True
        if not(node.is_goal()) and not self.goal and do =="goal":
            self.grid[row][col].make_goal()
            self.goal = True
        if not(node.is_barrier()) and not(node.is_start()) and not(node.is_goal()) and do =="barrier":
            self.grid[row][col].make_barrier()
        







    def gap_between(self, rows, width):
        return width // rows  # how many columns in the screen width


    def searching_algorithms(self, algorithm, start, goal):
        #for pixels value into the Grid location
        start = (start[0] // self.gap_between(self.rows, self.width), start[1] // self.gap_between(self.rows, self.width))
        goal = (goal[0] // self.gap_between(self.rows, self.width), goal[1] // self.gap_between(self.rows, self.width))
        start  = self.grid[start[0]][start[1]]
        goal  = self.grid[goal[0]][goal[1]]
        print(start, goal)
        if algorithm == "BFS":
            bfs = BFS()
            bfs.BFS_algorithm(self.grid, start, goal, self.rows)



