
STRING = ['a', 'b', 'c', 'd']

def reverse_string(string_list):

    left_index = 0
    right_index = len(string_list) - 1

    while left_index < right_index:

        string_list[left_index], string_list[right_index] = \
            string_list[right_index], string_list[left_index]

        left_index += 1
        right_index -= 1

    return string_list

if __name__ == '__main__':
    print(reverse_string(STRING))