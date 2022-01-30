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


# from queue import PriorityQueue
# from time import sleep
# M = []
# path_cost = 1
# #make matrix
# for i in range(5):
#     M.append([])
#     for j in range(5):
#         M[i].append((i,j))


# # print matrix
# for i in M:
#     for j in i:
#         print(j , end = ' ')
#     print()
# print()
# print()


# def calc_heuristic(start, goal):
#     return abs(goal[0]-start[0])+abs(goal[1]-start[1])
# def neighbours(start):
#     neighbours = []
#     #up
#     if start[0] + 1>=0 and (start[0] + 1)<5:
#         neighbours.append([start[0]+1, start[1]])
#     #down
#     if start[0]  -1>=0 and (start[0]  -1)<5:
#         neighbours.append([start[0]-1, start[1]] )
#     #right
#     if start[1] + 1>=0 and (start[1] + 1)<5:
#         neighbours.append([start[0], start[1]+1])
#     #left
#     if start[1] - 1>=0 and (start[1] - 1)<5:
#         neighbours.append([start[0], start[1]-1])

#     return neighbours



# def Astar_Algorithm(grid, start, goal):
#     open_set = PriorityQueue()
#     func = path_cost + calc_heuristic(start, goal)
#     open_set.put([func, start])
#     closed_set = []
#     came_from = []
    

#     while open_set is not open_set.empty():
#         item = open_set.get()
#         if item[1] in closed_set:
#             continue
#         came_from.append(item)
#         if item[1] == goal:
#             return item[1], came_from, open_set
#         closed_set.append(item[1])
#         for each in neighbours(item[1]):
            
#             func = path_cost + calc_heuristic(each, goal)
            
#             open_set.put([func, each])
            




# print(Astar_Algorithm(M, [0,0], [4,0] )[0])


# def BFS_Algorithm(grid, start, goal):
#     open_set = PriorityQueue()
#     func = calc_heuristic(start, goal)
#     open_set.put([func, start])
#     closed_set = []
#     came_from = []
    

#     while open_set is not open_set.empty():
#         item = open_set.get()
#         print(item)
#         if item[1] in closed_set:
#             continue
#         came_from.append(item)
#         if item[1] == goal:
#             return item[1], came_from, open_set
#         closed_set.append(item[1])
#         for each in neighbours(item[1]):
            
#             func = calc_heuristic(each, goal)
            
#             open_set.put([func, each])
            




# print(BFS_Algorithm(M, [0,0], [3,3] )[0])








