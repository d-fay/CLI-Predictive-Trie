"""

Trie object is a trie data structure and associated methods,
including support for completing strings based on prefix input.

More information about the Trie data structure:
 - https://www.toptal.com/java/the-trie-a-neglected-data-structure
 - https://en.wikipedia.org/wiki/Trie

REQUIREMENT: python2.7

"""


class WordTrie(object):

    # localizes variables
    def __init__(self):
        self.children = {}
        self.flag = False   # Flag to represent that a word ends at this node

    # inserts a character into the trie structure (accepts only single characters)
    def add_char(self, char):
        self.children[char] = WordTrie()    # recursive call to trie data structure

    # inserts a word (or sequence of characters) into the trie structure (accepts a string)
    def insert_word(self, word):
        node = self
        for char in word:
            if char not in node.children:
                node.add_char(char)
            node = node.children[char]
        node.flag = True

    # checks if a word (or sequence of characters) is exists in the trie structure (accepts a string)
    def contains_word(self, word):
        node = self
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.flag

    # returns list of all suffixes matching the provided prefix param (accepts a prefix string)
    def get_all_suffixes(self, prefix):
        results = set()
        if self.flag:
            results.add(prefix)
        if not self.children:
            return results
        # reduce(func, seq) : continually applies func() to the sequence & returns a single value.
        # In this case we use to find all possible suffixes by following each child node
        return reduce(lambda a, b: a | b, [node.get_all_suffixes(prefix + char)
                                           for (char, node) in self.children.items()]) | results

    # returns list of all words contained in the trie structure that match the provided prefix param (string)
    def get_all_possible_words(self, prefix):
        node = self
        for char in prefix:
            if char not in node.children:
                return set()
            node = node.children[char]
        return list(node.get_all_suffixes(prefix))
