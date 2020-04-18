import string
pangram = "The quick, brown fox jumps over the lazy dog!"

# This is a really good example of how you can use set logic, what they did what compare
# the string.ascii_lowercase to a set of s.lower

def is_pangram(s):
    # aset = set()
    # for char in s:
    #     if char not in aset:
    #         aset.add(char)
    #
    # if len(aset) >= 26:
    #     return True
    # else:
    #     return False
    return True if len(set(s.lower())) >= 26 else False # this is also another solution


def is_pangram_theirs(s):
    return set(string.ascii_lowercase) <= set(s.lower())

print(string.ascii_lowercase)

print(is_pangram(pangram))