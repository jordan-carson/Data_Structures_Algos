def flip(arr, k):
    pivot = (k + 1) // 2
    for i in range(0, pivot):
        tmp = arr[i]
        arr[i], arr[k - 1] = arr[k - 1], tmp

def pancakeSort(arr):
    for i in range(len(arr)-1, 1):
        maxindex = findMaxIndexInPrefix(arr, i)
        flip(arr, maxindex)
        flip(arr, i)
    return arr

def findMaxIndexInPrefix(arr, k):
    ans = 0
    for i in range(k):
        if arr[i] > arr[ans]:
            ans = i
    return ans

def sortPancakes(stack):

    sorted_index = 10
    for i in reversed(range(len(stack))):
        stack = flip(stack, findLargestPancake(stack, i))
        print("Flip Up", stack)
        stack = flip(stack, i)
        print("Flip Down", stack)
    return stack


# All of the pancakes are sorted after index
# Returns the index of largest unsorted pancake
def findLargestPancake(stack, index):

    largest_pancake = stack[index]
    largest_index = index;

    for i in range(index):
        if stack[i] > largest_pancake:
            largest_pancake = stack[i]
            largest_index = i

    print("Insert Spatula in index", largest_index, "Size", largest_pancake)
    return largest_index

# Slide spatula under pancake at index and flip to top
def flip(stack, index):
    newStack = stack[:(index + 1)]
    newStack.reverse()
    newStack += stack[(index + 1):]
    return newStack



arr = [1, 5, 4, 3, 2]
print(sortPancakes(arr))