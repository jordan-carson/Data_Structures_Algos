def sqrt(number):
    if not isinstance(number, int):
        print('TypeError')
        # continue
        return None
    if number in [0, 1]:
        return number

    start, end = 1, number

    while start <= end:
        mid_index = (start + end) // 2
        mid_squared = mid_index * mid_index

        if mid_squared == number:
            return mid_index

        elif mid_squared > number:
            end = mid_index - 1
        else:
            start = mid_index + 1
            answer = mid_index
    return answer


def sqrt_fast(number):
    if not isinstance(number, int) or number is None:
        # print('Not a number')
        return None
    if number in [0, 1]:
        return number
    return int(number ** (1/2))



if __name__ == '__main__':

    # Create a pointer to which function we want to use!
    sqrt = sqrt_fast

    # Regular tests
    print ("Pass" if  (3 == sqrt(9)) else "Fail")
    print ("Pass" if  (4 == sqrt(16)) else "Fail")
    print ("Pass" if  (5 == sqrt(27)) else "Fail")

    # Edge Cases
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (None == sqrt(None)) else 'Fail')

    # Large Number Tests
    print('Pass' if (9999 == sqrt(99999999)) else 'Fail')
    print('Pass' if (29814239699 == sqrt(888888888888888888888)) else 'Fail')
    print('Pass' if (35136 == sqrt(1234567890)) else 'Fail')