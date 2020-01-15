class HuffmanCodingNode:
    def __init__(self, char, frequency):
        self.char = char
        self.freq = frequency
        self.left, self.right = None, None


class HuffmanCoding:
    def encode(self):
        pass

    def decode(self):
        pass

    def _create_frequencies(self, text, as_dict=False):
        freq = dict()
        for ch in text:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1
        return [HuffmanCodingNode(temp_ch, temp_freq) for temp_ch, temp_freq in freq.items()] if not as_dict else freq

    def _sort_frequencies(self, text):
        return sorted(self._create_frequencies(text), key=lambda x: x.freq, reverse=True)


def text_to_frequency_dict(text):
    freq_dict, final = dict(), list()
    for char in text:
        if char not in freq_dict.keys():
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1
    for char, freq in freq_dict.items():
        final.append(HuffmanCodingNode(char, freq))
    return final


if __name__ == '__main__':
    text_to_frequency_dict('jordan')