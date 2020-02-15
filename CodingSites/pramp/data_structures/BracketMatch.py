def bracket_match(text):
    stack = list()
    len_stack = 0
    position = 0
    closing = 0
    while position < len(text):
        symbol = text[position]
        if symbol == '(':
            stack.append(symbol)
            # len_stack += 1
        else:
            if stack == [] and symbol == ')':
                closing += 1
            else:
                stack.pop()
                # len_stack -= 1
        position += 1

    if stack != []:
        return False
    return len(stack)
    # if stack != []:
    #     return len(stack) + closing
    # else:
    #     return closing

print(bracket_match('))))'))

# print(bracket_match('((3^2 + 8)*(5/2))/(2+6)'))


def bracket_match(text):
    counter = 0
    ans = 0
    n = len(text)

    for i in range(0, n-1):
        if text[i] == '(':
            counter += 1
        elif text[i] == ')':
            counter -= 1

        if counter < 0:
            counter += 1
            ans += 1
    return ans + counter

print(bracket_match('))))'))


def bracket_match(text):
    stack = []
    for bracket in text:
        if bracket == "(":
            stack.append(bracket)
        elif bracket == ")":
            if len(stack) != 0 and stack[-1] == "(":  # matching
                stack.pop(-1)
            else:
                stack.append(bracket)
    return len(stack)


# print bracket_match("(()")
print(bracket_match("))))"))

# print bracket_match("(()")
print(bracket_match("))))"))
