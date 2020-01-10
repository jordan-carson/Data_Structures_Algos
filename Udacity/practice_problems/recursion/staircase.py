

def staircase(n):
    """
    Write a function that returns the number of steps you can climb a staircase that
    has n steps.

    You can climb in either 3 steps, 2 steps or 1 step.

    Example:
        n = 3
        output = 4

        1. 1 step +  1 step + 1 step
        2. 1 step + 2 steps
        3. 2 steps + 1 step
        4. 3 steps
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


if __name__ == '__main__':
    print(staircase(4) == 7)
    print(staircase(3) == 4)

