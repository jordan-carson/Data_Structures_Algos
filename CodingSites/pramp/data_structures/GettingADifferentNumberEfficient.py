def get_different_number(arr):
    largest = max(arr)
    out = [None for _ in range(largest+1)]
    for a in arr:
        out[a] = a
    for i in range(len(out)):
        if out[i] is None:
            return i
    return len(out)