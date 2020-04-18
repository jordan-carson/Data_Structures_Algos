from collections import defaultdict
from typing import Union, List


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False

    ## Initialize this node in the Trie
    def suffixes(self, suffix=''):
        suffixes = list()
        for char, node in self.children.items():
            if node.is_word is True:
                suffixes.append(suffix + char)
            if node.children:
                suffixes.extend(node.suffixes(suffix + char))
        return suffixes


## Recursive function that collects the suffix for
## all complete words below this point


class Trie:
    def __init__(self):
        self.root = TrieNode()
    ## Initialize this Trie (add a root node)

    def insert(self, word):
        # simplifying the insert operation
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_word = True

    def find(self, prefix):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None
        return current_node

    def does_word_exist(self, word) -> bool:
        """
        Does this word exist in our trie?
        @param word: word
        @return: Boolean
        """
        node = self.find(word)
        if node:
            return node.is_word
        else:
            return False


if __name__ == '__main__':
    # Add words

    trie = Trie()
    wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
    ]

    for word in wordList:
        trie.insert(word)

    assert trie.does_word_exist('ant') is True

    # Testing Suffixes
    node = trie.find("t")
    # suffixes, counter = node.suffixes()
    print(node.suffixes()) # ['nt', 'nthology', 'ntagonist', 'ntonym']
    print(node.counter)
    # assert node.suffixes() == ['nt', 'nthology', 'ntagonist', 'ntonym']
    node = trie.find("f")
    # print(node.suffixes()) # ['un', 'unction', 'actory']
    assert node.suffixes() == ['un', 'unction', 'actory']

    node = trie.find('')
    # print(node.suffixes()) # ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie', 'trigger', 'trigonometry', 'tripod']
    assert node.suffixes() == ['ant', 'anthology', 'antagonist', 'antonym', 'fun', 'function', 'factory', 'trie',
                               'trigger', 'trigonometry', 'tripod']

    # Testing does_word_exist(word) method
    assert trie.does_word_exist('ant') is True
    assert trie.does_word_exist('factory') is True
    assert trie.does_word_exist('jordan') is False

    # from ipywidgets import widgets
    # from IPython.display import display
    # from ipywidgets import interact
    # def f(prefix):
    #     if prefix != '':
    #         prefixNode = MyTrie.find(prefix)
    #         if prefixNode:
    #             print('\n'.join(prefixNode.suffixes()))
    #         else:
    #             print(prefix + " not found")
    #     else:
    #         print('')
    # interact(f,prefix='');