"""
Basic Regex Parser
Implement a regular expression function isMatch that supports the '.' and '*' symbols. The function receives two strings - text and pattern - and should return true if the text matches the pattern as a regular expression. For simplicity, assume that the actual symbols '.' and '*' do not appear in the text string and are used as special symbols only in the pattern string.

In case you aren’t familiar with regular expressions, the function determines if the text and pattern are the equal, where the '.' is treated as a single a character wildcard (see third example), and '*' is matched for a zero or more sequence of the previous letter (see fourth and fifth examples). For more information on regular expression matching, see the Regular Expression Wikipedia page.

Explain your algorithm, and analyze its time and space complexities.

Examples:

input:  text = "aa", pattern = "a"
output: false

input:  text = "aa", pattern = "aa"
output: true

input:  text = "abc", pattern = "a.c"
output: true

input:  text = "abbb", pattern = "ab*"
output: true

input:  text = "acd", pattern = "ab*c."
output: true
Constraints:

[time limit] 5000ms
[input] string text
[input] string pattern
[output] boolean
"""


def is_match(text, pattern):
    if len(pattern) == 0:
        return len(text) == 0

    # if the length of pattern is 1
    if len(pattern) == 0 or pattern[1] != '*':
        if len(text) < 1 or (pattern[0] != '.' and text[0] != pattern[0]):
            return False
        return is_match(text[1:], pattern[1:])
    else:
        i = -1
        while (i < len(text) and (i < 0 or pattern[0] == '.' or pattern[0] == text[i])):
            if is_match(text[i + 1], pattern[2:]):
                return True
            i += 1
    return False


print(is_match('aa', 'aa'))