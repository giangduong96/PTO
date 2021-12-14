"""
You are given a nested list of integers nestedList. Each element is either an integer or a list whose elements may also be integers or other lists. Implement an iterator to flatten it.

Implement the NestedIterator class:

NestedIterator(List<NestedInteger> nestedList) Initializes the iterator with the nested list nestedList.
int next() Returns the next integer in the nested list.
boolean hasNext() Returns true if there are still some integers in the nested list and false otherwise.
Your code will be tested with the following pseudocode:

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
If res matches the expected flattened list, then your code will be judged as correct.
"""


class NestedIterator(object):
    def __init__(self, nestedList):
        self.l = self._flatten(nestedList)
        self.i = -1

    def _flatten(self, l):
        l2 = []
        for ele in l:
            if ele.isInteger():
                l2.append(ele.getInteger())
            else:
                l2.extend(self._flatten(ele.getList()))
        return l2

    def next(self):
        self.i += 1
        return self.l[self.i]

    def hasNext(self):
        return self.i < len(self.l) - 1


def run(array):
    res = []
    for ele in array:
        if isinstance(ele, int):
            res.append(ele)
        else:
            res.extend(run(ele))
    return res

nestedList = [[1,1],2,[1,1,[12,32]]]
print(run(nestedList))
