"""
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
"""


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """

    if not isinstance(number, int):
        raise TypeError(f'{number} is not of integer type, but instead {type(number)}')

    if number in [0, 1]:
        return number

    start, end = 1, number

    while start <= end:
        # print(start, end)
        mid = (start + end) // 2
        mid_squared = mid * mid
        # print(mid_squared)
        if mid_squared == number:
            return mid
        elif mid_squared > number:
            end = end - 1
        else:
            start = start + 1
            ans = mid
    return ans


def sqrt_fast(number):
    if not isinstance(number, (int, float)):
        return None
    if number in [0, 1]:
        return number
    return int(number ** (1.0/2))




print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")