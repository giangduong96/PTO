"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.


Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
"""
import collections


def hasGroupSizeX(array):
    counter = collections.Counter(array)
    print(counter)

    if all(v % 2 == 0 for v in counter.values()):
        return True
    return False


deck = [1, 2, 3, 4, 4, 3, 2, 1]
deck2 = [1, 1, 1, 2, 2, 2, 2, 3, 3]
print(hasGroupSizeX(deck))
print(hasGroupSizeX(deck2))
