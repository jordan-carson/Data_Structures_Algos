# Uses python3
import sys


def merge(a, b, count):
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            res.append(b[j])
            count[0] += len(a) - i
            j += 1
        else:
            res.append(a[i])
            i += 1
    res.extend(a[i:])
    res.extend(b[j:])
    return res


def merge_sort(a, count):
    if len(a) < 2:
        return a
    mid = len(a) // 2
    return merge(merge_sort(a[:mid], count), merge_sort(a[mid:], count), count)


def get_number_of_inversions(a):
    count = [0]
    sorted = merge_sort(a, count)
    return count[0]

# def get_number_of_inversions(a, b, left, right):
#     number_of_inversions = 0
#     if right - left <= 1:
#         return number_of_inversions
#     ave = (left + right) // 2
#     number_of_inversions += get_number_of_inversions(a, b, left, ave)
#     number_of_inversions += get_number_of_inversions(a, b, ave, right)
#     #write your code here
#     return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(merge_sort(a, n))  # , b, 0, len(a)
