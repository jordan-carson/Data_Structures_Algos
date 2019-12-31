def basic_op1(operator, value1, value2):
    if operator=='+':
        return value1+value2
    if operator=='-':
        return value1-value2
    if operator=='/':
        return value1/value2
    if operator=='*':
        return value1*value2

def basic_op2(operator, value1, value2):
    return eval("{}{}{}".format(value1, operator, value2))


print(basic_op1('/', 49, 7))