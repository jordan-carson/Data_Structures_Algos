# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt
T = int(input())

def isPrime(n):
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True


for _ in range(T):
    num = int(input())
    if num >= 2 and isPrime(num):
        print('Prime')
    else:
        print('Not prime')



