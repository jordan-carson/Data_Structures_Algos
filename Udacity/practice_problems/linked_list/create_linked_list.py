from Data_Structures_Algos.Udacity.practice_problems.linked_list import Node


def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list:
    @return:
    """
    head = None

    for value in input_list:
        if head is None:
            head = Node(value)
        else:
            current_node = head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(value)

    return head


if __name__ == '__main__':
    ### Test Code
    def test_function(input_list, head):
        try:
            if len(input_list) == 0:
                if head is not None:
                    print("Fail")
                    return
            for value in input_list:
                if head.value != value:
                    print("Fail")
                    return
                else:
                    head = head.next
            print("Pass")
        except Exception as e:
            print(f"Fail: {e}")

    input_list = [1, 2, 3, 4, 5, 6]
    head = create_linked_list(input_list)
    test_function(input_list, head)

    input_list = [1]
    head = create_linked_list(input_list)
    test_function(input_list, head)

    input_list = []
    head = create_linked_list(input_list)
    test_function(input_list, head)
