
def get_min_max(ints):
   first_index = 0
   last_index = len(ints) -1

   min = ints[0]
   max = ints[-1]
   while first_index < last_index:
    print(first_index, last_index)
    if ints[first_index] < min:
        min = ints[first_index]
    else:
        first_index += 1

    if ints[last_index] > max:
        max = ints[last_index]
    else:
        last_index -= 1

    last_index -= 1
    first_index += 1
    return [min, max]


print(get_min_max([2,3,4,6,7,892,3,5,23,4,3]))