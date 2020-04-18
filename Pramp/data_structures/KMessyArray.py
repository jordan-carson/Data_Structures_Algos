import heapq


def sort_k(arr, k):

    # create a list of the first k + 1 elements
    heap = arr[:k + 1]

    heapq.heapify(heap)

    target_index = 0
    for i in range(k + 1, len(arr)):
        arr[target_index] = heapq.heappop(heap)
        heapq.heappush(heap, arr[i])
        target_index += 1

    while heap:
        arr[target_index] = heapq.heappop(heap)
        target_index += 1

    return arr





k = 3
arr = [2, 6, 3, 12, 56, 8]
print(sort_k(arr, k))