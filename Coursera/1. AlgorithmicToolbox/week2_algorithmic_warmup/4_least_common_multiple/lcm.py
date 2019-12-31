# Uses python3
import sys
def gcd_euclid(a, b):
    if b == 0:
        return a

    aprime = a % b
    return gcd_euclid(b, aprime)

def lcm_naive(a, b):
    # for l in range(1, a*b + 1):
    #     if l % a == 0 and l % b == 0:
    #         return l
    #
    # return a*b
    return (a // gcd_euclid(a, b)) * b

# print(lcm_naive(10, 20))

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

