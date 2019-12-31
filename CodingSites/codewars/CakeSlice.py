def cake_slice(num):
    num_slices = 0

    for i in range(1, num + 1):

        if i == 1:
            num_slices = 2
        elif i == 2:
            num_slices = 4
        else:
            num_slices = i + num_slices

    return num_slices

def cake_slice_theirs(n):
    #coding and coding...
    sum = 1
    for i in range(n):
        sum += i+1
        print(i, sum)
    return sum


def cake_slice2(n):
    return (n ** 2 + n + 2) // 2

print(cake_slice2(10))