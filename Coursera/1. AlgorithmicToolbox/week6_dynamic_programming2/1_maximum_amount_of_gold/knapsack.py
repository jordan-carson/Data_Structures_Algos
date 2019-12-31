# Uses python3
import sys
# from tqdm import tqdm
import pprint


def optimal_weight(W, w):
    # write your code here

    mem = [[0 for _ in range(W+1)] for _ in range(len(w))]

    # build table mem[][] in bottom up manner
    for j in range(len(w)):
        for i in range(W+1):
            if w[j] > i:
                mem[j][i] = mem[j - 1][i]
            else:
                mem[j][i] = max(w[j] + mem[j - 1][i - w[j]], mem[j - 1][i])
    pprint.pprint(mem)
    return mem[len(w)-1][W]
    # result = 0
    # for x in w:
    #     if result + x <= W:
    #         result = result + x
    # return result


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
