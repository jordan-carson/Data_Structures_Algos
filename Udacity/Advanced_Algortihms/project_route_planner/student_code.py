# https://www.redblobgames.com/pathfinding/a-star/introduction.html
# https://github.com/fafl/priority-queue/blob/master/priority_queue.py

# from .priority_queue import PriorityQueue
import heapq
from Data_Structures_Algos.Udacity.Advanced_Algortihms.project_route_planner.priority_queue import PriorityQueue

"""

For every path finding operation we have a GRAPH (M), a starting node (start), and an end node (goal). 
We need to find the most optimal / shortest path from the starting node to the end node within the given GRAPH.

Pseudocode for A* a.k.a A_Star

OPEN // set of node to be evaluated
CLOSED // set of nodes already evaluated

loop
    current = node in OPEN with the lowest f_cost (videos say the cost starts at 0).
    remove current from OPEN
    add current to CLOSED
    
    if current is equal to the target
        return 
    
    foreach neighbor of the current node
        if neighbor is not traversable or neighbor is in CLOSED
            skip to the next neighbor
        
        if new path to neighbor is shorter OR neighbor is not in OPEN
            set the f_cost of the neighbor
            set the parent of neighbor to current
            if neighbor is not in OPEN
                add neighbor to open 
"""


def heuristic_sqrt(origin, destination):
    return ((origin[0] - destination[0]) ** 2 + (origin[1] - destination[1]) ** 2) ** (1 / 2)


def heuristic(origin, destination):
    return ((origin[0] - destination[0]) ** 2 + (origin[1] - destination[1]) ** 2)


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def shortest_path(M, start, goal):
    return a_star(M, start, goal)


def dikstras(graph, start, end):
    raise NotImplementedError


def distance(x, y):
    return ((y[0] - x[0])**2 + (y[1] - x[1])**2)**(1/2)


# def a_star_final(graph, start, goal):
#     queue = PriorityQueue()
#     queue.enqueue(start, 0)
#
#     explored






def a_star(graph, start, goal):
    came_from = dict()
    came_from[start] = None

    cost_dict = dict()
    cost_dict[start] = 0
    # frontier = PriorityQueue()
    # frontier.insert((start, 0))
    frontier = [(0, start)]

    while len(frontier) > 0:
        current = heapq.heappop(frontier)[1]
        if current == goal:
            break

        for next in graph.roads(current):

            # we need to calculate the path cost now
            cpath_cost = heuristic(graph.intersections[current], graph.intersections[next])
            new_cost = cost_dict[current] + cpath_cost

            if next not in cost_dict or new_cost < cost_dict[next]:
                came_from[next] = current
                cost_dict[next] = new_cost
                heapq.heappush(frontier, ())
                # priority = heuristic(goal, next)
                # frontier.insert(next, priority)
                # came_from[next] = current
