# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# 2 pointer O(n) O(min (m,n) Space
def longestSubstring(string):
    chars = [0] * 128

    left = right = 0
    res = 0
    while right < len(string):
        r = string[right]
        chars[ord(r)] += 1

        while chars[ord(r)] > 1:
            l = string[left]
            chars[ord(l)] -= 1
            left += 1
        res = max(res, right - left + 1)

        right += 1
    return res


print(longestSubstring("pwwkew"))

# hashmap O(n) O(min (m,n) Space
def longestSubStringHashMap(string):
    n = len(string)
    ans = 0
    dict = {}
    left = 0
    for right in range(n):
        # if character at pointer right already in dict, move left pointer to position
        # which after last occurs of right pointer
        if string[right] in dict.keys():
            left = max(dict[string[right]], left)

        # find max each time
        ans = max(ans, right - left + 1)
        # update values of right pointer where its duplicated
        dict[string[right]] = right +1
    return ans


print(longestSubstring("pwwkew"))
print(longestSubStringHashMap("abcdeafbdgcbb"))