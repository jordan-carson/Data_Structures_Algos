def myInt(s):
    num = 0
    if len(s) == 0:
        raise TypeError("Input string must be non-empty")
    if len(s) is None:
        raise TypeError("Input string must not be None")

    sign = 1

    if s[0] == "-":
        sign = -1
        s = s[1:]

    power = 0
    for i in range(len(s)-1, -1, -1):
        if ord(s[i]) in range(ord("0"), ord("9")+1):
            num += (ord(s[i]) - ord("0")) * 10**power
            power += 1
        else:
            raise TypeError("Input string must contain only digits and minus sign")

    return sign * num


print(myInt('0'))