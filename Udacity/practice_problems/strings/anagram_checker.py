# Code

def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """
    if len(str1) != len(str2):
        # remove the spaces and lower the strings
        str1_update = str1.replace(' ', '').lower()
        str2_update = str2.replace(' ', '').lower()

        if len(str1_update) == len(str2_update):
            if ''.join(sorted(str1_update)) == ''.join(sorted(str2_update)):
                return True
    return False




if __name__ == '__main__':
    # Test Cases

    print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
    print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
    print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
    print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
    print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")
