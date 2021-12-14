"""
n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
"""

def numberOfOneBits(n):
    sum = 0
    while n != 0:
        sum += 1
        n = n & (n-1)
    return sum
n = 4
print(numberOfOneBits(n))