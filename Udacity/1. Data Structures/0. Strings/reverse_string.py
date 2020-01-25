def string_reverser(our_string, solution = 'Jordan'):

    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """
    new_string = ''
    for i in range(len(our_string)):
#         print( 'This', (len(our_string) - 1) - i)
        new_string += our_string[(len(our_string) - 1) - i]
    return our_string[::-1] if solution == 'Jordan' else new_string



if __name__ == '__main__':
    # Test Cases

    print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
    print(
        "Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail"
    )
    print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")