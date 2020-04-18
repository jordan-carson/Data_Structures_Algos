

def largest_subarray_with_amount(outfits, amo):
    # Write your code here

    summary = dict()
    total = 0
    maxLen = 0

    for i in range(len(outfits)):
        total += outfits[i]
        if total == amo:
            total = i + 1
        if not total in summary:
            summary[total] = i

        if (total - amo) in summary:
            # if the component is in our dictionary set maxLen = to i - val
            if maxLen < (i - summary.get(total - amo)):
                maxLen = i - summary.get(total - amo)
    return maxLen

print(largest_subarray_with_amount([1, 1, 2, 1, 20, 1, 1, 1, 1, 1, 3], 7))