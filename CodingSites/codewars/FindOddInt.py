from collections import Counter
from timeit import Timer


def find_it(seq):
    return [k for k, v in Counter(seq).items() if v % 2 != 0][0]
        # print(v % 2)


def find_it_theirs(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return 1


t1 = Timer("find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])", "from __main__ import find_it")
print("using my solution", t1.timeit(number=10000), 'milliseconds')
t2 = Timer('find_it_theirs([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])', "from __main__ import find_it_theirs")
print('using theirs', t2.timeit(number=10000), 'milliseconds')


print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))