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
        return len(stack) + closing
    else:
        return closing

print(bracket_match('(()()'))