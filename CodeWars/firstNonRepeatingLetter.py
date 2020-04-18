from collections import Counter
def firstNonRepeatingCharacter(s):
    # lowercase everything
    # or casefold
    # if a string contains all repeating characters it should return a empty string
    order = []
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
            order.append(char)
    for x in order:
        if counts[x] == 1:
            return x
    return ""

print(firstNonRepeatingCharacter('stress'))