from collections import deque


def reverse_words(arr):
    # ["perfect", "makes", "practice"]

    # Iterate through the array, and
    # append them to a stack
    stack = list()

    s = deque()
    for i in range(len(arr)):
        if arr[i] != ' ':
            stack.append(arr[i])  # [ 'p', 'e', 'r', 'f', 'e', 'c', 't'.
        else:
            s.appendleft(stack)
            s.appendleft(" ")
            # final_list.insert(0, " ")
            stack = list()
    s.appendleft(stack)
    return list(inner for outer in s for inner in outer)


arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]
print(reverse_words(arr))