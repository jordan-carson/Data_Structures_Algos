# Add the Node class here


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        # if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head  # place the new node at the head (top) of the linked list
            self.head = new_node

        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None

        value = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


if __name__ == '__main__':
    # Setup
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.push(40)
    stack.push(50)

    # Test size
    print("Pass" if (stack.size() == 5) else "Fail")

    # Test pop
    print("Pass" if (stack.pop() == 50) else "Fail")

    # Test push
    stack.push(60)
    print("Pass" if (stack.pop() == 60) else "Fail")
    print("Pass" if (stack.pop() == 40) else "Fail")
    print("Pass" if (stack.pop() == 30) else "Fail")
    stack.push(50)
    print("Pass" if (stack.size() == 3) else "Fail")

    """
    
    Time complexity of stacks using linked lists

    Notice that if we pop or push an element with this stack, there's no traversal. 
    We simply add or remove the item from the head of the linked list, and update the `head` reference. 
    So with our linked list implementaion, `pop` and `push` have a time complexity of O(1).
    
    Also notice that using a linked list avoids the issue we ran into when we implemented our stack using an array. 
    In that case, adding an item to the stack was fine—until we ran out of space. 
    Then we would have to create an entirely new (larger) array and copy over all of the references from the old array.
    
    That happened because, with an array, we had to specify some initial size 
    (in other words, we had to set aside a contiguous block of memory in advance). 
    But with a linked list, the nodes do not need to be contiguous. 
    They can be scattered in different locations of memory, an that works just fine. 
    This means that with a linked list, we can simply append as many nodes as we like. 
    Using that as the underlying data structure for our stack means that we never run out of capacity, 
    so pushing and popping items will always have a time complexity of O(1).
    
"""