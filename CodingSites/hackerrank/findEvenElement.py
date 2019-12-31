
# find even occurring element in a list

sample = [1, 1, 1, 3, 3]
import collections
def getEvenNumber(arr):

    counts = collections.defaultdict(int)
    print(counts)
    for num in arr:
        counts[num] += 1
    print(counts)
    for k, v in counts.items():
        if v % 2 == 0:
            return k

print(getEvenNumber(sample))