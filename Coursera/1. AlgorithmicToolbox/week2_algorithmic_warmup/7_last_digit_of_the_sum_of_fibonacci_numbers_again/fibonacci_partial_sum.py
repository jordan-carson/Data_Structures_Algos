# Uses python3
import sys

def fibonacci_partial_sum_naive(m, n):
    if m > n:
        return

    # Collect 60 Fibonnaci numbers
    a = [0, 1]
    for i in range(2, 60):
        a.append(a[i-1] + a[i-2])

    # Simplify the input arguments, as the last digit pattern repeats with a period of 60,
    # and the sum of 60 such consecutive numbers is 0 mod 10:
    m = m % 60
    n = n % 60
    # Make sure n is greater than m
    if n < m:
        n += 60

    su = 0
    for j in range(m, n+1): # Assume n index is inclusive
        su += a[j % 60]

    return su % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))