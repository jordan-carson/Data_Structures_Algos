# Problem 4

This problem was solved using several pointers to guide us where the starting, ending locations
to where the 0, 1, 2 are stored in the final array. Performing a while loop until the middle and end
are equal or the middle is greater than the end. During this process, we sort the array in-place.

Thus the time and space complexities are:

Time Complexity: 
O(n) as we loop through the entire array and is sorted in one traversal. 

Space Complexity: 
O(1), sorting is done in-place with the assistance of a `swap()` function. No additional memory is required.