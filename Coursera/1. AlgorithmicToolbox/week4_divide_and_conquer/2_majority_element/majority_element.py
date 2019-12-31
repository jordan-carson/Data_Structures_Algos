# Uses python3
import sys

def get_majority_element(a, left, right):
    # if left == right:
    #     return -1
    # if left + 1 == right:
    #     return a[left]
    # #write your code here
    # return -1

    count, possible_element = 0, None
    for num in a:
        if count == 0:
            possible_element = num
            count += 1
        elif num == possible_element:
            count += 1
        else:
            count -= 1

    count = 0
    for num in a:
        if num == possible_element:
            count += 1

    if count > len(a) / 2:
        return possible_element
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # print(get_majority_element(a, 0, len(a)))

    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
