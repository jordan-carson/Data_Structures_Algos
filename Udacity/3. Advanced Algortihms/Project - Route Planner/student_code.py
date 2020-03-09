# https://www.redblobgames.com/pathfinding/a-star/introduction.html
# https://github.com/fafl/priority-queue/blob/master/priority_queue.py

from .priority_queue import PriorityQueue


def manhattan_distance(b, a):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def shortest_path(M, start, goal):
    return a_star_search(M, start, goal)


def dikstras(graph, start, end):
    raise NotImplementedError


def a_star_search(graph, start, goal):
    came_from = dict()
    came_from[start] = None

    frontier = PriorityQueue()
    frontier.insert((start, 0))

    while not frontier.empty():
        # current = frontier.()
        # current =

        if current == goal:
            break

        for next in graph.neighbors(current):
            if next not in came_from:
                priority = heuristic(goal, next)
                frontier.insert(next, priority)
                came_from[next] = current
