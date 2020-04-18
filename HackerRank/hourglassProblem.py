# given an array of size 6x6, A:

# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0

# an hourglass in A is to be a subset of values with indices falling in the pattern below:

# a b c
#   d
# e f g

# there are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass's values
# calculate the hourglass sum for every hourglass in A, then print the max hourglass sum

arr = []  # Define the array

# Input elements of Matrix and put it into array
for arr_i in range(6):
    arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
    arr.append(arr_t)

print(arr)
# Define an array for storing output
a = []

# Calculate the total for each hourglass
for i in range(0, 4):
    for j in range(0, 4):
        total = arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + \
                arr[i + 2][j + 2]
        a.append(total)

# Print the Max value of total in the array
print(max(a))