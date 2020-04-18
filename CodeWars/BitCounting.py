def countBits(n):
    num_bits = 0
    while n:
        num_bits += n & 1
        n >>= 1
    return num_bits

print(countBits(1234))


def countBits2(n):
    return bin(n).count("1")


from timeit import Timer

t1 = Timer("countBits(1234)", "from __main__ import countBits")
print("using my solution", t1.timeit(number=10000), 'milliseconds')
t2 = Timer('countBits2(1234)', "from __main__ import countBits2")
print('using theirs', t2.timeit(number=10000), 'milliseconds')

print(countBits2(1234))