# https://leetcode.com/problems/encode-and-decode-strings/solution/

# time O(N), space O(1)
class Code():
    def __init__(self):
        self.passcode = '#$%'


    def encode(self, strs):
        res = ''
        for strr in strs:
            res += str(len(strr)) + self.passcode + strr
        return res


    def decode(self,s):
        res = []
        i = 0
        while i < len(s):
            p = s.find(self.passcode, i)
            length = int(s[i:p])
            res.append(s[p + len(self.passcode):p + len(self.passcode) + length])
            i = p + len(self.passcode) + length
        return res

m=  Code()
message = m.encode(["hello", "world"])
print(message)
print(m.decode(message))