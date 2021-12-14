# https://leetcode.com/problems/design-add-and-search-words-data-structure/
import collections

# time O(N^2 * M) where N is number of inserted key, M is key length
class WordDictionary:
    def __init__(self):
        self.dict = collections.defaultdict(set)

    def addWord(self, word):
        self.dict[len(word)].add(word)

    def searchWordd(self, word):
        m = len(word)

        for dict_word in self.dict[m]:
            i = 0
            while i < m and (dict_word[i] == word[i] or word[i] == '.'):
                i += 1
            if i == m:
                return True
        return False

# tree approach
class WordDictTree:
    def __init__(self):
        self.tree = {}

    def addWord(self, word):
        node = self.tree

        for ch in word:
            if not ch in node:
                node[ch] ={}
            node = node[ch]
        
