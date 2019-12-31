# Uses python3
import sys

def fibonacci_sum_naive(number):
    # if n <= 1:
    #     return n
    #
    # previous = 0
    # current  = 1
    # sum      = 1
    #
    # for _ in range(n - 1):
    #     previous, current = current, previous + current
    #     sum += current
    #
    # return sum % 10
    PISANO = 60  # 1

    if number < 2:
        return number

    number %= PISANO

    results = [1, 1]
    for _ in range(number):  # 2
        results.append((results[-1] + results[-2]) % 10)  # 3

    return (results[-1] - 1) % 10  # 4


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
