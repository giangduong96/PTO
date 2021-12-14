# https://leetcode.com/problems/longest-palindromic-substring/

# Time O(N^2) Space O(N)
def longestCommonPalindrome(string):
    if string == "" or len(string) < 1:
        return ""
    res = ""
    for i in range(len(string)):
        oddcase = helper(string, i, i)
        if len(oddcase) > len(res):
            res = oddcase
        evencase = helper(string, i, i + 1)
        if len(evencase) > len(res):
            res = evencase
    return res


def helper(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return string[left+1: right]


print(longestCommonPalindrome('babad'))
