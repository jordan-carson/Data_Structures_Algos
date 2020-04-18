def merge_two_lists(left, right):
    merged = list()
    left_idx = 0
    right_idx = 0

    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] > right[right_idx]:
            merged.append(right[right_idx])
            right_idx += 1
        else:
            merged.append(left[left_idx])
            left_idx += 1

    merged += left[left_idx:]
    merged += right[right_idx:]
    return merged


