# Problem 1

This problem I decided to solve two different ways. 

`sqrt()` 

Time Complexity: The time complexity is O(n), as we loop through the entire number -> n, until we reach the mid_squared.
Space Complexity: Memory is independent to input. Each loop run is independent. 

`sqrt_fast()
`

To review a square root, lets go over an example. The square root of 4 for instance, is asking what number
can be multiplied by themselves once in order to give 4? This is obvious, as the answer is 2 x 2.
as well as (-2) x (-2). 

If you do the math out, this breaks down into raising to the power of 1/2.
Thus the square root of 4 is equal to 4^(1/2). Which is 2. 


Time Complexity: O(1)
Space Complexity: O(1)