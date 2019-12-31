# Uses python3
import sys, math
# def fast_detect_pisano_period(pisano_table):
#     # Instead of check left_half pisano_table equal right_half pisano_table.
#     # We just need to check first ten elements of left_half equal to ten elements of right_half.
#     pisano_table[len(pisano_table)-10] == 0 and
#     pisano_table[size-9] == 1 and
#     pisano_table[0:10] == pisano_table[(size-10):size]

def get_fibonacci_huge_naive(n, m):
    # # Initialize a matrix [[1,1],[1,0]]
    v1, v2, v3 = 1, 1, 0
    # Perform fast exponentiation of the matrix (quickly raise it to the nth power)
    for rec in bin(n)[3:]:
        calc = (v2*v2) % m
        v1, v2, v3 = (v1*v1+calc) % m, ((v1+v3)*v2) % m, (calc+v3*v3) % m
        if rec == '1': v1, v2, v3 = (v1+v2) % m, v1, v2
    return v2
#     if n <= 1:
#         return n
#
#     previous = 0
#     current = 1
#
#     pisano_table = []
#     for i in range(n -1):
#         # loop(n - 1)
#         times:
#         pisano_table.append(previous % m)
#         previous, current = current, previous + current
#         if fast_detect_pisano_period(pisano_table):
#         # now, we have pisano table, we just get index for pisano_table at reminder of n % period
#             return pisano_table[n % period]
#
#
# return current % m



if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
