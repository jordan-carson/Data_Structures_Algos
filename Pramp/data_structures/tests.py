from collections import deque


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


root = Node(0)
n1 = Node(5)
n2 = Node(3)
n3 = Node(6)
n1.parent = root
n2.parent = root
n3.parent = root
root.children = [n1, n2, n3]

n4 = Node(4)
n5 = Node(2)
n6 = Node(0)
n7 = Node(1)
n8 = Node(5)

n4.parent = n1
n1.children = [n4]

n5.parent = n2
n6.parent = n2
n2.children = [n5, n6]

n7.parent = n3
n8.parent = n3
n3.children = [n7, n8]

n9 = Node(1)
n9.parent = n5
n5.children = [n9]

n10 = Node(10)
n10.parent = n6
n6.children = [n10]

n11 = Node(1)
n11.parent = n9
n9.children = [n11]

print(get_cheapest_cost(root))
