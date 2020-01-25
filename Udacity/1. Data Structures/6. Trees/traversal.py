# this code makes the tree that we'll traverse


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


def traverse(tree, direction='pre order'):

    if not isinstance(tree, Tree):
        raise TypeError('Tree is not a tree instance')

    visited = list()

    def pre_order(node):
        if node:
            visited.append(node.get_value())

            pre_order(node.get_left_child())

            pre_order(node.get_right_child())

    def post_order(node):
        if node:
            # traverse left subtree
            post_order(node.get_left_child())

            # traverse right subtree
            post_order(node.get_right_child())

            # visit node
            visited.append(node.get_value())

    def in_order(node):

        if node:
            # traverse left subtree
            post_order(node.get_left_child())
            # visit node
            visited.append(node.get_value())
            # traverse right subtree
            post_order(node.get_right_child())

    f = {'pre order': pre_order, 'post order': post_order, 'in order': in_order}
    f[direction](tree.get_root())
    return visited



if __name__ == '__main__':
    # create a tree and add some nodes
    tree = Tree("apple")
    tree.get_root().set_left_child(Node("banana"))
    tree.get_root().set_right_child(Node("cherry"))
    tree.get_root().get_left_child().set_left_child(Node("dates"))

    print(tree.get_root())
    print(traverse(tree))

    tree.get_root()
    print(traverse(tree, 'in order'))
