def get_sum(a, b):
    getmin = min(a, b)
    getmax = max(a, b)
    new_sum = 0
    for i in range(getmin, getmax+1):
        new_sum += i

    return new_sum


# print
print(get_sum(-1, 3))