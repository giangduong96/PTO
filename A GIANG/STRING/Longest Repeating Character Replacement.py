# https://leetcode.com/problems/longest-repeating-character-replacement/
# longest repeating character replacement

# sliding window
def characterReplacement(string, k):
    n = len(string)
    left, right = 0 , 0
    ans = 0
    while right < n:
        if string[left] != string[right]:
            k -= 1
            while k < 0:
                if string[left] == string[right]:
                    k += 1
                left += 1
        ans = max(ans, right - left + 1)
        right += 1
    return ans

s = "AABABBA"
k = 1
print(characterReplacement(s, k))