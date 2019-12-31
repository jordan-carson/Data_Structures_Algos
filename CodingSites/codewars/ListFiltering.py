def filter_list(l):
    'return a new list with the strings filtered out'
    new_list = []
    for i in l:
        if not isinstance(i, str):
            new_list.append(i)
    return new_list


print(filter_list([12,3,'lullabye']))
