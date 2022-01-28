from queue import PriorityQueue

class BFS:

    def BFS_algorithm(self, grid, start, goal):
        open_set = PriorityQueue()
        heur = self.calc_heuristic(start, goal)
        open_set.put([heur, start])
        closed_set = []
        came_from = []


        while open_set is not open_set.empty():
            item = open_set.get()
            node = item[1]
            if node in closed_set:
                continue
            came_from.append(item)
            if node == goal:
                return node, came_from, open_set
            closed_set.append(node)
            for each in neighbours(grid, node):

                heur = self.calc_heuristic(each, goal)

                open_set.put([heur, each])
        

    def cal_heuristic(self, start, goal):
        start_row, start_col = start.get_pos()
        goal_row, goal_col = goal.get_pos()

        return abs(goal_row - start_row) + abs(goal_col - start_col)
