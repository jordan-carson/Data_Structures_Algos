# Create a hashtable
# loop through the array, if find an element that is not in
# the array, I am going to take the complement being 21 - i
# and add that to the hashtable, otherwise I am going to return
# hashtables key[num], and the current iterator

def get_indices_of_item_wights(arr, limit):
    # edge cases
    if len(arr) == 0 or len(arr) <= 1:
        return []

    buffer = {}

    for i in range(len(arr)):
        if arr[i] in buffer:
            return [i, buffer[arr[i]]]
        else:
            buffer[limit - arr[i]] = i

# ##
# def getIndicesOfItemWeights(arr, limit):
#     m = new
#     Map()
#
#     for index from 0 to arr.length - 1:
#         w = arr[index]
#         complementIndex = m.findKey(limit - w)
#         if (complementIndex != null):
#             return [index, complementIndex]
#         else:
#             m.insert(w, index)
#
#     return null