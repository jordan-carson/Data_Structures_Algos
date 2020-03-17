import math
from provided_graphs import Map10, Map40
from data_structures import PriorityQueue
# import heapq

"""
# https://www.redblobgames.com/pathfinding/a-star/introduction.html

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

        if neighbor is not in OPEN OR new path to neighbor is shorter (i.e. the new cost is less than the cost of the neighbor)
            set the f_cost of the neighbor
            set the parent of neighbor to current
            if neighbor is not in OPEN
                add neighbor to open 
"""

"""
Let's go over the algorithm one more time before we start coding this thing...
We start with a graph, and we want to find the shortest path between a starting node and an end node. 
Recall graphs can be directed or undirected. Map10 shows a undirected graph, with a disconnected network of 10 
intersections. Two intersections [8,9] are connected to each other by they are not connected to the rest of the road
network. 

Map40 is provided which shows a network of roads which spans 40 different intersections (0 to 39). 
I have created my own abstraction of these maps within the provided_graphs.py file. 

A* - Algorithm Pseudo Code

Init a came_from dictionary to store all nodes -> neighbors, set the came_from[start] = None
Init a COST_DICT to store all path costs, set the start_node = 0 cost_dict[start] = 0

initialize a Frontier PriorityQueue (Heapq or custom class)
enqueue the start node, with 0 priority

loop
    pop the item with the lowest cost, this can be done with the dequeue method
    if the current node = our goal
        break
        
    foreach neighbor of the current node
        calculate the path cost between the current_node and the neighbor
        calculate the new cost, which is the current node cost + the path cost
        
        if the neighbor is not in our COST_DICT OR the calculated NEW_COST is less than the cost of the neighbor
            update the neighbors cost dict with the new cost
            
            calculate the priority by calculating the new_cost + distance between the neighbor and the goal
            
            enqueue within our frontier the neighbor and the calculated priority
            
            update the CAME_FROM dictionary assigning the neighbor equals to the current_node

finally
    find the best_path using the CAME_FROM, START & GOAL
    While the goal does not equal the start
        add the current node to our final list
        update the current node from the came_from dictionary
    
    return the reversed list
"""

def calculate_distance(origin, destination):
    return ((origin[0] - destination[0]) ** 2 + (origin[1] - destination[1]) ** 2) ** (1 / 2)


def heuristic(origin, destination):
    return ((origin[0] - destination[0]) ** 2 + (origin[1] - destination[1]) ** 2)


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def shortest_path(M, start, goal):
    return a_star(M, start, goal)


def dijkstra(graph, start, goal):
    distance_dict = {node: float('inf') for node in graph.nodes}
    shortest_path_to_node = dict()

    distance_dict[start] = 0

    while distance_dict:
        # pop the shortest_path
        current_node, node_distance = sorted(distance_dict.items(), key=lambda x: x[1])[0]
        shortest_path_to_node[current_node] = distance_dict.pop(current_node)

        for edge in current_node.edges:
            if edge.node in distance_dict:
                new_node_distance = node_distance + edge.distance
    return shortest_path_to_node[goal]


def a_star(graph, start, goal):
    came_from = dict()
    came_from[start] = None

    cost_dict = dict()
    cost_dict[start] = 0

    # Using a custom Priority Queue class instead of heapq, cleaner
    frontier = PriorityQueue()
    frontier.enqueue(start, 0)
    # frontier = [(0, start)]
    # while len(frontier) > 0:
    while not frontier.is_empty():
        # popped_item = frontier.dequeue()
        # current, priority = popped_item.element, popped_item.priority
        current, priority = frontier.pop_item()
        # current = heapq.heappop(frontier)[1]
        if current == goal:
            break

        for next in graph.roads[current]:
            # we need to calculate the path cost now, which is the total cost through the current point to the next point
            path_cost = calculate_distance(graph.intersections[current], graph.intersections[next])
            new_cost = cost_dict[current] + path_cost

            if next not in cost_dict or new_cost < cost_dict[next]:
                # we need to record the best path
                cost_dict[next] = new_cost

                # calculating the priority from the next road to the goal road
                priority = new_cost + calculate_distance(graph.intersections[next], graph.intersections[goal])

                # add this to the frontier
                frontier.enqueue(next, priority)

                came_from[next] = current
    # print(came_from)
    # print(cost_dict)
    return best_path(came_from, start, goal)


def best_path(came_from, start, goal):
    current = goal
    path = list()
    try:
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
    except KeyError:
        return None
    # path.reverse()
    # print(path)
    return path[::-1]


def compare_output():
    print(f"Finding Shortest Path in Map10: Start: 0, Goal: 2\n\t Result = [0, 5, 3, 2]:{shortest_path(Map10(), 0, 2)}")
    print(f'Finding Shortest Path in Map10: Start: 6, Goal: 8\n\t Result = None:{shortest_path(Map10(), 6, 8)}')
    print(f'Finding Shortest Path in Map40: Start: 5, Goal: 34\n\t '
          f'Result = [5, 16, 37, 12, 34]:{shortest_path(Map40(), 5, 34)}')
    print(f'Finding Shortest Path in Map40: Start: 8, Goal: 24\n\t '
          f'Result = [8, 14, 16, 37, 12, 17, 10, 24]: {shortest_path(Map40(), 8, 24)}')
    print(f'Finding Shortest Path in Map40: Start: 5, Goal: 5\n\t Result = [5]:{shortest_path(Map40(), 5, 5)}')


if __name__ == "__main__":
    compare_output()
    test_cases = [
        # Provided Tests
        {'start': 8, 'goal': 24, 'graph': Map40(), 'result': [8, 14, 16, 37, 12, 17, 10, 24]},
        {'start': 5, 'goal': 34, 'graph': Map40(), 'result': [5, 16, 37, 12, 34]},
        {'start': 5, 'goal': 5, 'graph': Map40(), 'result': [5]},

        # Map 10 Sample Tests
        {'start': 0, 'goal': 2, 'graph': Map10(), 'result': [0, 5, 3, 2]},
        {'start': 6, 'goal': 8, 'graph': Map10(), 'result': None},

    ]

    def t_func(test_cases):
        for test in test_cases:
            print('Pass' if test['result'] == shortest_path(test['graph'], test['start'], test['goal']) else 'Fail')

    t_func(test_cases)
    # test maps
    # from data_structures_algos.project_4.helpers import Map, load_map, show_map
    # # from helpers import Map, load_map, show_map
    # map_10 = load_map("map-10.pickle")
    # map_40 = load_map("map-40.pickle")
    # # example 1
    # shortest_path(map_40, 8, 24)  # path: [8, 14, 16, 37, 12, 17, 10, 24]
    # # example 2
    # shortest_path(map_10, 2, 0)  # path: [2, 3, 5, 0]
    # # example 3
    # shortest_path(map_10, 3, 9)
    # compare_output()
    #
    #     test_cases = [
    #         [0, 5, 3, 2], [5, 16, 37, 12, 34], [8, 14, 16, 37, 12, 17, 10, 24]
    #     ]
    #
    #
    #     main()