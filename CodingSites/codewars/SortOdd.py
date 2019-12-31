
def sort_array(source_array):
    odds = iter(sorted(i for i in source_array if i % 2 != 0))
    return [next(odds) if i % 2 else i for i in source_array]


def sort_array(source_array):
    b = sorted([item for item in source_array if item % 2 != 0])
    odd_int = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = b[odd_int]
            odd_int += 1

    return source_array


print(sort_array([5, 3, 2, 8, 1, 4]))