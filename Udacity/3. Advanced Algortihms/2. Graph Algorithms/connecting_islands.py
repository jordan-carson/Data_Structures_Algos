import heapq


def create_graph(num_islands, bridge_config):
    adjacency_list = [list() for _ in range(num_islands + 1)]

    for config in bridge_config:
        source = config[0]
        destination = config[1]
        cost = config[2]
        adjacency_list[source].append((destination, cost))
        adjacency_list[destination].append((source, cost))
    return adjacency_list


def get_minimum_cost(graph):
    # set starting vertex to 0
    start_vertex = 0
    # initialize a list of Booleans (False) for the visited list
    visited = [False for _ in range(len(graph) + 1)]

    # initialize a starting list to keep track of vertices that are visited,- (edge_cost, neighbor)
    heap = [(0, start_vertex)]
    # set the total cost to 0
    total_cost = 0
    # loop through the heap using a while loop
    while len(heap) > 0:
        # pop the first element of the heap, which has a cost, and current_vertex
        cost, current_vertex = heapq.heappop(heap)
        # check if the current_vertex exists in the visited list
        if visited[current_vertex]:
            continue
        # else add the cost to total_cost
        total_cost += cost
        # for loop through the graph[current_vertex] neighbor, edge_cost
        for neighbor, edge_cost in graph[current_vertex]:
            # inside the loop push the (edge_cost, neighbor) into the heap
            heapq.heappush(heap, (edge_cost, neighbor))
        # finally mark the current_vertex as visited
        visited[current_vertex] = True
    # return the total cost
    return total_cost


def get_minimum_cost_of_connecting(num_islands, bridge_config):
    """
    :param: num_islands - number of islands
    :param: bridge_config - bridge configuration as explained in the problem statement
    return: cost (int) minimum cost of connecting all islands
    """
    graph = create_graph(num_islands, bridge_config)

    return get_minimum_cost(graph)

