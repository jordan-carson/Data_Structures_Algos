# Uses python3
# import sys, pprint
#
# def get_change(m):
#     #write your code here
#
#     money = m
#     mem = [0 for _ in range(m)]
#     pprint.pprint(mem)
#
#     # denominations = [1, 3, 4]
#
#
#
#     return m // 4
#
# if __name__ == '__main__':
#     m = int(sys.stdin.read())
#     print(get_change(m))
import collections

col = collections.defaultdict(list)

var = [1, 2, 3]
for val in var:
    col[val].append([1, 2, 3])

print(col[1])
