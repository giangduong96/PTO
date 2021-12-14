# https://leetcode.com/problems/top-k-frequent-words/
import collections


def topKFrequent(words, k):
    counter = collections.Counter(words)
    counter = [(c, counter[c]) for c in counter]
    # quan trong o day, sort theo -x[1] then sort theo x
    counter.sort(key=lambda x: (-x[1], x))
    result = []
    for i in range(k):
        result.append(counter[i][0])
    return result