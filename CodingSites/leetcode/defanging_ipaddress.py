class Solution:
    def defangIPaddr(self, address: str) -> str:
        """
        Input: address = "255.100.50.0"
        Output: "255[.]100[.]50[.]0"
        @param address:
        @return:
        """
        output = list()
        for idx, val in enumerate(address.split('.')):
            output.append(val)
            if not idx == len(address.split('.')) -1:
                output.append('[.]')
        return ''.join(output)



#
print(Solution().defangIPaddr('255.100.50.0'))
#

addresss = '255.100.50.0'
print(len(addresss.split('.')))

# print(list(["100.100.100".split('.')]))