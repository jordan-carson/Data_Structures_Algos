

def power_of_2(n):
    if n == 0:
        return 1
    return 2 * power_of_2(n - 1)


def print_integers(n):
    if n <= 0:
        return
    print(n)
    print_integers(n - 1)



print(power_of_2(5))