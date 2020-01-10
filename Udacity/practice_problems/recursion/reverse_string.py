# Code

def reverse_string_iterative(input):
    """
    Return reversed input string

    Examples:
       reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """

    # TODO: Write your recursive string reverser solution here

    if input == 0:
        return ""
    else:
        first_char = input[0]

    new_sring = list()
    for ch in range(len(input) - 1, -1, -1):
        new_sring.append(input[ch])
    return ''.join(new_sring)  # pass


def reverse_string_recursive(input_string):
    if len(input_string) == 0:
        return ""
    else:
        first_char = input_string[0]
        rest_of_chars = slice(1, None)  # input_string
        sub_string = input_string[rest_of_chars]

        reversed_string = reverse_string_recursive(sub_string)
        return reversed_string + first_char


if __name__ == '__main__':
    print(reverse_string_recursive("cba"))

    # Test Cases

    print("Pass" if ("" == reverse_string("")) else "Fail")
    print("Pass" if ("cba" == reverse_string("abc")) else "Fail")

