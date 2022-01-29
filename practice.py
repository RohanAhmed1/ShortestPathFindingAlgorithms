# from queue import PriorityQueue
# frontier  = PriorityQueue()
# print(frontier.put((2, "Rohan")))
# print(frontier.get()[1])
# start.make_open()
#         # algorithm
#         open_set = PriorityQueue()
#         heur = self.cal_heuristic(start, goal)
#         open_set.put([heur, start])
#         closed_set = []
#         came_from = []


#         while open_set is not open_set.empty():
#             item = open_set.get()
#             # item[1] is the node and item[0] is the heuristic of that node
#             node = item[1]
#             if node.is_open():
#                 came_from.append(item)
#                 if node == goal:
#                     return
#                 node.make_closed()
#                 for each in node.has_neighbours(grid, rows):
#                     if each is not each.is_closed():
#                         heur = self.cal_heuristic(each, goal)

#                         open_set.put([heur, each])
#                         each.make_open()



# if each is not each.is_closed():
#                     heur = self.cal_heuristic(each, goal)

#                     open_set.put([heur, each])
#                     each.make_open()



# def BFS_algorithm(self, grid, start, goal, rows):
#         # algorithm
#         open_set = PriorityQueue()
#         heur = self.cal_heuristic(start, goal)
#         open_set.put([heur, start])
#         closed_set = []
#         came_from = []


#         while open_set is not open_set.empty():
#             item = open_set.get()
#             # item[1] is the node and item[0] is the heuristic of that node
#             node = item[1]
#             if node in closed_set:
#                 continue
#             came_from.append(item)
#             if node == goal:
#                 return 
#             closed_set.append(node)
#             node.make_closed()
#             for each in node.has_neighbours(grid, rows):
#                  heur = self.cal_heuristic(each, goal)
#                  open_set.put([heur, each])
#                  if not each.is_closed():
#                     each.make_open()

#         return "not found"