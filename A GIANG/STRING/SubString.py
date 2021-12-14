"""
https://leetcode.com/problems/implement-strstr/
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
"""


# KMP approach O(m+n) space O(N)
def subString(long, short):
    # find prefix also a suffix in short string
    prefix = [0] * len(short)
    i, j = 0, 1
    while j < len(short):
        if short[i] == short[j]:
            prefix[j] = i + 1
            i += 1
            j += 1
        else:
            if i == 0:
                i == 0
            else:
                i = prefix[i - 1]
            # if short[i] != short[j]:
            #     prefix[j] = 0
            j += 1

    # use pattern matching to find substring
    l, s = 0, 0
    while l < len(long) and s < len(short):
        if long[l] == short[s]:
            l += 1
            s += 1
        else:
            if s == 0:
                l += 1
            else:
                s = prefix[s - 1]

    return l - len(short) if s == len(short) else -1


print(subString("abcdeabmkabeieabceiabcedb", "iabce" ))