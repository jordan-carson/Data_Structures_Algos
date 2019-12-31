def get_cheapest_cost_system_answer(rootNode):
    n = rootNode.children

    if n == 0:
        return rootNode.cost
    else:
        minCost = 10000
        for i in range(n-1):
            tempcost = get_cheapest_cost(rootNode.children[i])
            if tempcost < minCost:
                minCost = tempcost
    return minCost + rootNode.cost



def get_cheapest_cost(rootNode):
    # we need to find the minimum total cost
    # 1. loop through the children nodes, and return the minimum cost
    # 2.
    total_cost = rootNode.cost
    # edge cases
    result = 100000
    if len(rootNode.children) == 0:
        return total_cost

    # 0 is our current rootNode
    # its children are 5, 3, 6
    # 0 -> 5 -> 4 -> 3 -> 2 -> 1 -> 1 ->....
    for child in rootNode.children:
        result = min(result, get_cheapest_cost(child))
        total_cost += result
    return total_cost


##########################################
# Use the helper code below to implement #
# and test your function above           #
##########################################

# A node
class Node:

    # Constructor to create a new node
    def __init__(self, cost):
        self.cost = cost
        self.children = []
        self.parent = None





