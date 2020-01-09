def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.

    Args:
       input(str): input to be checked if it is palindrome
    """

    # TODO: Write your recursive palindrome checker here
    if len(input) <= 1:
        return True
    else:
        first = input[0]
        last = input[-1]

        sub_input = input[1:-1]

    return (first == last) and is_palindrome(sub_input)


if __name__ == "__main__":
    # Test Cases

    print("Pass" if (is_palindrome("")) else "Fail")
    print("Pass" if (is_palindrome("a")) else "Fail")
    print("Pass" if (is_palindrome("madam")) else "Fail")
    print("Pass" if (is_palindrome("abba")) else "Fail")
    print("Pass" if not (is_palindrome("Udacity")) else "Fail")
