import heapq


class HuffmanNode:
    def __init__(self, char, frequency):
        self.char = char
        self.freq = frequency
        self.left, self.right = None, None

    def is_leaf(self):
        return not (self.left or self.right)

    def is_right(self):
        return self.right is True

    def is_left(self):
        return self.left is True


class HuffmanCoding:
    """
    A Huffman code is a type of optimal prefix code that is used for compressing data.
    The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to
    make it smaller, there is no loss of information.

    The Huffman algorithm works by assigning codes that correspond to the relative frequency of each
    character for each character. The Huffman code can be of any length and does not require a prefix;
    therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

    There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building
    a Huffman tree, encoding the data, and, lastly, decoding the data.

    Here is one type of pseudocode for this coding schema:

            Take a string and determine the relevant frequencies of the characters.
            Build and sort a list of tuples from lowest to highest frequencies.
            Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more
                frequent letters. (This is the heart of the Huffman algorithm.)
            Trim the Huffman Tree (remove the frequencies from the previously built tree).
            Encode the text into its compressed form.
            Decode the text from its compressed form.
            You then will need to create encoding, decoding, and sizing schemas.
    """
    def __init__(self):
        self.data = dict()

    def encode(self):
        pass

    def decode(self):
        pass

    # def search(self):

    def _create_frequencies(self, text, as_dict=False):
        """Take a string and determine the relevant frequencies of the characters."""
        freq = dict()
        for ch in text:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
        # return [HuffmanNode(temp_ch, temp_freq) for temp_ch, temp_freq in freq.items()] if not as_dict else freq
        return freq

    def _sort_frequencies(self, text):
        import operator

        dic = self._create_frequencies(text)
        sorted_d = sorted(dic, key=dic.get, reverse=True)
        new_dict = dict()
        for val in sorted_d:
            new_dict[val] = dic[val]
        return new_dict
        # tup = ()
        # sorted_list = sorted(self._create_frequencies(text), key=lambda x: x.freq, reverse=True)
        # for ch, freq in self._create_frequencies(text).items():
        # return sorted_d
        # return sorted(self._create_frequencies(text), key=lambda x: x.freq, reverse=True)


def text_to_frequency_dict(text):
    freq_dict, final = dict(), list()
    for char in text:
        if char not in freq_dict.keys():
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1
    for char, freq in freq_dict.items():
        final.append(HuffmanNode(char, freq))
    return final


if __name__ == '__main__':
    text_to_frequency_dict('jordan')

    print(HuffmanCoding()._sort_frequencies('jordan carson'))