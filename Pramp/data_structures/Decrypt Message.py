def decrypt(word):
    '''
    enc[n] = dec[n] ....
    '''
    decrypted = ''
    step = 1

    for char in word:
        ascii_char = ord(char)
        ascii_char -= step
        step += ascii_char
        while ascii_char < ord('a'):
            ascii_char += 26

        decrypted += chr(ascii_char)
    return decrypted


import unittest


class Test(unittest.TestCase):
    inputs = [
        ("flgxswdliefy", "encyclopedia"),
        ("dnotq", "crime")
    ]

    def test_decyption(self):
        for [test_case, expected] in self.i:
            actual = decrypt(test_case)
            self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()


"""
function decrypt(word):
    secondStep = 1
    decryption = ""

    for i from 0 to word.length - 1:
        newLetterAscii = asciiValue(word[i])
        newLetterAscii = newLetterAscii - secondStep

        while (newLetterAscii < asciiValue('a')):
            newLetterAscii += 26

        decryption = decryption + asciiToChar(newLetterAscii)
        secondStep += newLetterAscii

    return decryption
"""