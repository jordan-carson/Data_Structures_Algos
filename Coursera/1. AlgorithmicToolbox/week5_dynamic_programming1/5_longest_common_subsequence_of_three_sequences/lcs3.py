#Uses python3

import sys
import numpy as np
def lcs3(a, b, c):
    mem = [[[0 for _ in range(len(c) + 1)] for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]

    for i in range(len(a)+1):
        for j in range(len(b)+1):
            for k in range(len(c)+1):
                if i == 0 or j == 0 or k == 0:
                    mem[i][j][k] = 0
                    continue
                elif a[i - 1] == b[j - 1] and a[i - 1] == c[k - 1]:
                    mem[i][j][k] = mem[i-1][j-1][k-1] + 1
                    continue
                else:
                    # mem[i][j][k] = max(max(mem[i-1][j][k], mem[i][j-1][k]),
                    #                 mem[i][j][k-1])
                    mem[i][j][k] = max(mem[i - 1][j][k], mem[i][j - 1][k], mem[i][j][k - 1],
                                       mem[i - 1][j - 1][k], mem[i - 1][j][k - 1], mem[i][j - 1][k - 1])
    return mem[len(a)][len(b)][len(c)]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    # print(a, b, c)
    print(lcs3(a, b, c))
