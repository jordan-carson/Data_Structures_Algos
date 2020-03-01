# Problem 2

For this problem I decided to solve using a binary search algorithm,
at first I tried to find the pivot point, which wasn't working as
well as I expected. Than I tried solving this using a recursive, and 
solving the problem in one pass. My final solution using a recursive function
`_rotated_array_search` which takes in the input_list, left, right, and the number we are searching. 
This function uses conditional tests to determine the recursion via **Binary 
Search Algorithm**.  


Time Complexity: 
O(log n)

Space Complexity: 
O(log n), for recursive implementation due to call stack.
