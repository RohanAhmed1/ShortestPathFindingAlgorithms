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
            # item[1] is the node and item[0] is the heuristic of that node
            node = item[1]
            if node in closed_set:
                continue
            came_from.append(item)
            if node == goal:
                return node, came_from
            closed_set.append(node)
            for each in node.has_neighbours(grid):

                heur = self.calc_heuristic(each, goal)

                open_set.put([heur, each])

        return "not found"
        

    def cal_heuristic(self, start, goal):
        start_row, start_col = start.get_pos()
        goal_row, goal_col = goal.get_pos()

        return abs(goal_row - start_row) + abs(goal_col - start_col)
