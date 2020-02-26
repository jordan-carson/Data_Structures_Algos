# Problem 3

The sample output to this problem shows [542, 31] or [531, 42]. The latter puts the even and odd numbers together 
in order of largest to smallest. From the lessons, this problem can be solved using a Heap, in fact a MaxHeap.
I modified the Heap from the lessons into a CustomHeap class. And popped each number from the heap, 
comparing if the number is even or odd and putting the output together.

Time Complexity: 
O(n log n). This is due to our heap data sturcture, the heapify and popping of elements from our heap both take
take O(n log n), while creating the output takes linear O(n) time. Thus overall, O(n log n).

Space Complexity: 
O(n) This is due to our heap data structure, which creates a new array from the input size n. 
So our space does grow to size O(n). 
