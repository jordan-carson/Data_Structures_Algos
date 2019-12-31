# Uses python3
import sys, math

def get_fibonacci_last_digit_naive(n):
    final_array = [0, 1]
    for i in range(2, n+1):
        final_array.append(final_array[-1] % 10 + final_array[- 2] % 10)

    return final_array[-1] % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
