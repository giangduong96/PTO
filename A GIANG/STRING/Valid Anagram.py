# https://leetcode.com/problems/valid-anagram/
import collections


def validAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    dict = {}
    for ch in str1:
        dict.get(ch, 1)
    for ch in str2:
        dict.get(ch, -1)
    if sum(dict.values()) == 0:
        return True
    return False


# counter
def validAnagramCounter(str1, str2):
    if len(str1) != len(str2):
        return False
    str1_Counter = collections.Counter(str1)
    str2_Counter = collections.Counter(str2)

    return str1_Counter == str2_Counter


s = 'anagram'
t = 'nagaram'
print(validAnagramCounter(s, t))
print(validAnagram(s, t))
