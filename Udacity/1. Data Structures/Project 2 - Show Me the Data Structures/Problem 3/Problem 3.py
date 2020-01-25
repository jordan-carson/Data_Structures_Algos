import sys


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left, self.right = None, None

    def __add__(self, other):
        return self.freq + other.freq

    def __sub__(self, other):
        return self.freq - other.freq

    def __str__(self):
        return f'Node:{self.char}: {self.freq} \t -> {self.left} <- {self.right} '


class HuffmanCoding:
    def __init__(self):
        # self.text = text
        self.encoded_dict = dict()
        self.encoded_text = ''
        self.decoded_text = ''
        self.frequency_dict = dict()

    def _create_frequencies(self, text):
        """
        Create a list of character frequencies.
        :param text:
        :return:
        """

        frequency = dict()
        # calculate the word frequencies, add them to a dictionary
        for char in text:
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1
        self.frequency_dict = frequency
        # iterate over the items of the dictionary to store them in a list
        return [Node(char, freq) for char, freq in frequency.items()]

    @staticmethod
    def _sort_frequencies(freq):
        """
        You can eliminate the need of using the sorting function by utilizing the min-heap as a data structure.
        Python's heapq library provides an implementation of this.
        """
        return sorted(freq, key=lambda x: x.freq, reverse=True)

    def decode(self, encoded_text, tree):
        """
        Function to decode the encoded_text
        :param encoded_text:
        :param tree:
        :return:
        """
        decoded_data = ''
        if encoded_text == '':
            return decoded_data
        current_node = tree

        for char in encoded_text:
            if char == '0': # set it to the left
                current_node = current_node.left
            elif char == '1': # set to the right
                current_node = current_node.right
            else:
                raise ValueError('Char is not either a 0 or 1')

            if current_node.char is not None:
                decoded_data += current_node.char
                current_node = tree
        self.decoded_text = decoded_data
        return decoded_data

    def create_encoding_dict(self, tree):
        if tree.left is None and tree.right is None: return {tree.char: '0'}
        return self._create_encoding_dict(tree, '')

    def _create_encoding_dict(self, tree, current_code):
        codes = dict()
        if tree is None: return dict()
        if tree.char is not None:
            codes[tree.char] = current_code
        # elif tree.left is None and tree.right is None:
        #     return {tree.char: '0'}
        # left is 0, right is 1
        codes.update(self._create_encoding_dict(tree.left, current_code + '0'))
        codes.update(self._create_encoding_dict(tree.right, current_code + '1'))
        self.encode_dict = codes
        return codes

    def create_merged_trie(self, text):
        """
        Create a frequency Trie, where we store the letter and frequency, as well as pointers to the left or
        right nodes.

        1. First get a sorted list of frequencies List[tuples]
        2. Iterate through popping the first two elements and storing the total frequency as a new parent node.
        3. Add the parent node back into the frequencies list. (Re sort)

        :param text:
        :return:
        """
        frequencies = self._sort_frequencies(self._create_frequencies(text))

        # handling inputs of one
        if len(frequencies) == 1:
            node = frequencies.pop()
            new_node = Node(None, node.freq)
            new_node.left = node
            frequencies.append(new_node)

        while len(frequencies) > 1:
            left = frequencies.pop()
            right = frequencies.pop()
            parent = Node(None, left + right)
            parent.left, parent.right = left, right
            frequencies.append(parent)
            frequencies = self._sort_frequencies(frequencies)
        return frequencies[0]

    def create_total_dict(self, text):
        """
        Each key is a letter with the values being a list of the frequency, and decoded value.
        """
        tree = self.create_merged_trie(text)
        # freqs = self._create_frequencies(text)
        huff_map = self._create_encoding_dict(tree, '')
        output = dict()
        for ch in text:
            output[ch] = [self.frequency_dict[ch], huff_map[ch]]
            # output.append([ch, huff_map[ch], self.frequency_dict[ch]])
        return output


def huffman_encoding(text):
    """Initialize the Huffman Object
    1. Init the Huffman Object
    2. Create the Huffman Tree with the sorted frequencies within the Huffman Object
    3. Build a dictionary consisting off

    """
    if text == '': return '', None
    #     raise ValueError('Text input must have a length greater than 1')
    huffman = HuffmanCoding()
    huff_tree = huffman.create_merged_trie(text)
    huff_map = huffman.create_encoding_dict(huff_tree)
    encoded_data = ''
    for char in text:
        encoded_data += huff_map[char]
    return encoded_data, huff_tree


def huffman_decoding(encoded_text, tree):
    decoded_data = ''
    if encoded_text == '': return decoded_data
    current_node = tree

    for char in encoded_text:
        if char == '0':  # set it to the left
            current_node = current_node.left
        # elif char == '1':  # set to the right
        else:    current_node = current_node.right
        # else:
        #     raise ValueError('Char is not either a 0 or 1')

        # print(current_node.char)
        if current_node and current_node.char is not None:
            decoded_data += current_node.char
            current_node = tree
    return decoded_data


if __name__ == "__main__":
    huffman_coding = HuffmanCoding()

    a_great_sentence = "Hello World"
    print('Tests 1')

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = "Longer Sentence, but not a full paragraph."
    print('Tests 2')

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = "Answer 2"

    print('Tests 3')

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

    a_great_sentence = 'Just my Name, Jordan carson'

    print('Tests 4')

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    # print(huffman_coding.create_total_dict(a_great_sentence))

    print('Edge Tests - single letter') # 'AAAAAAAAAA' doesn't work

    a_great_sentence = 'AAAAAAA'

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))

    print('Emoty strng case ')
    a_great_sentence = ''

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(encoded_data)))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))