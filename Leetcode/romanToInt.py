class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Function to convert a Roman Numeral to Integer.
        Symbol       Value
        I             1
        V             5
        X             10
        L             50
        C             100
        D             500
        M             1000
        :param s: str
        :return: int
        """
        # if I before V then 5 - 1.
        # if I before X then 10 - 1
        # if I is before V or X then V or X - 1
        # if X is placed before L and C then L or C - 10
        # if C is placed before D and M then D or M - 100
        rom_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        for i in range(len(s)):
            x = rom_dict[s[i]]
            if i+1 < len(s) and rom_dict[s[i+1]] > x:
                total -= x
            else: total += x

        return total



if __name__ == '__main__':
    print(Solution().romanToInt('XXIV'))











