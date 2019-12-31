# Uses python3
import sys

def get_change_greedy(m, den):

    if m == 0:
        return []
    for i in den:
        if i <= m:
            return [i] + get_change_greedy(m-i, den)
    # #write your code here
    # amount_of_ten = int(m / d[0])
    # amount_of_five = int((m - amount_of_ten * d[0]) / d[1])
    # amount_of_one = int(m - amount_of_ten * d[0] - amount_of_five * d[1])
    # return amount_of_ten + amount_of_five + amount_of_one

def get_change_specific(value):
    p, n, d = 1, 3, 4
    count = 0
    while value > 0:
        if value >= d:
            count += value // d
            value %= d
        elif value >= n:
            count += value // n
            value %= n
        else:
            count += value // p
            break
    return count


print(get_change_specific(34))
#
# if __name__ == '__main__':
#     m = int(sys.stdin.read())
#     print(get_change(m))
