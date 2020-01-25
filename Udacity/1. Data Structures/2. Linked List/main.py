from Data_Structures_Algos.Udacity.practice_problems.linked_list.data_structure import Node, LinkedList
# from .data_structure import Node


def print_linked_list(head):
    current_node = head

    while current_node is not None:
        print(current_node.value)
        current_node = current_node.next





if __name__ == '__main__':
    input_list = [2,1,4,3,5]
    head = Node(input_list[0])
    head.next = Node(input_list[1])
    head.next.next = Node(input_list[2])
    head.next.next.next = Node(input_list[3])
    head.next.next.next.next = Node(input_list[4])
    print_linked_list(head)

    head2 = create_linked_list(input_list)
    print_linked_list(head2)

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
    # ll = create_linked_list()
    # print(head2.to_list())