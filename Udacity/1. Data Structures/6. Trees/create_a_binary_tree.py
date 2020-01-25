## your code here
## your code here
# add set_value and get_value functions
## Define a node


class Node:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def set_left_child(self, value):
        self.left = value

    def set_right_child(self, value):
        self.right = value

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None


# define a Tree class here
class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def get_root(self):
        return self.root


def pre_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            # visit the node
            visit_order.append(node.get_value())

            # traverse left subtree
            traverse(node.get_left_child())

            # traverse right subtree
            traverse(node.get_right_child())

    traverse(tree.get_root())

    return visit_order


# solution
def in_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())

            # visit node
            visit_order.append(node.get_value())

            # traverse right sub-tree
            traverse(node.get_right_child())

    traverse(tree.get_root())

    return visit_order


# solution
def post_order(tree):
    visit_order = list()

    def traverse(node):
        if node:
            # traverse left subtree
            traverse(node.get_left_child())

            # traverse right subtree
            traverse(node.get_right_child())

            # visit node
            visit_order.append(node.get_value())

    traverse(tree.get_root())

    return visit_order


if __name__ == '__main__':
    # create a tree and add some nodes
    tree = Tree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))

    node0 = Node()
    print(f"""
    value: {node0.value}
    left: {node0.left}
    right: {node0.right}
    """)

    ## Check

    node0 = Node()
    print(f"""
    value: {node0.value}
    left: {node0.left}
    right: {node0.right}
    """)

    node0 = Node("apple")
    print(f"""
    value: {node0.value}
    left: {node0.left}
    right: {node0.right}
    """)


    ## check

    node0 = Node("apple")
    node1 = Node("banana")
    node2 = Node("orange")
    node0.set_left_child(node1)
    node0.set_right_child(node2)

    print(f"""
    node 0: {node0.value}
    node 0 left child: {node0.left.value}
    node 0 right child: {node0.right.value}
    """)

    ## check

    node0 = Node("apple")
    node1 = Node("banana")
    node2 = Node("orange")

    print(f"has left child? {node0.has_left_child()}")
    print(f"has right child? {node0.has_right_child()}")

    print("adding left and right children")
    node0.set_left_child(node1)
    node0.set_right_child(node2)

    print(f"has left child? {node0.has_left_child()}")
    print(f"has right child? {node0.has_right_child()}")

    pre_order(tree)

