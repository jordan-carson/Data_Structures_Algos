class Solution:
    def reverse(self, x: int) -> int:
        if x is None or x == '0' or x == 0:
            return 0
        str_x = str(x)
        actual_x = int(x)
        negative = False
        if str_x[0] == '-':
            negative = True
            actual_x = actual_x * (-1)
            str_x = str_x[1:]
        # we need to now reverse the string
        str_x = str_x[::-1]
        count = 0
        for i in range(len(str_x)):
            if str_x[i] == '0':
                count += 1
            else:
                break
        str_x = str_x[count:] if negative == False else '-' + str_x[count:]
        if int(str_x) > 2147483647 or int(str_x) < -2147483647:
            return 0
        else:
            return int(str_x)


if __name__ == '__main__':
    s = Solution()
    x = s.reverse(120000)
    print(x)