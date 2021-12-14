"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1

"""

# use set() to check whether the new number n is repeated
def isHappy( n):
    def divde_square(x):
        s = 0
        while x > 0:
            x, mod = divmod(x, 10)
            s += (mod ** 2)
        return s

    if n == 1:
        return True

    _set = set()
    _set.add(n)
    while True:
        n = divde_square(n)
        if n == 1:
            return True
        if n in _set:
            return False
        _set.add(n)

def isHappy(num):
    slow = squared(num)
    fast = squared((squared(num)))

    while slow != fast and fast != 1:
        slow = squared(slow)
        fast = squared(squared(fast))
    return fast == 1


def squared(num):
    result = 0
    while num > 0:
        last = num % 10
        result += last * last
        num = num // 10
    return result

"""
 Floyd's Algorithm

Time complexity: O(c)*
Space complexity: O(1)

c = number of elements visited before cycle

Note*: Floyd's Hare and Tortoise algorithm uses less memory, but it can actually take longer
 to run than a traditional HashSet implementation. (it still works with Linear Time Complexity though,
 it's just a bit slower due to the higher number of repeated operations)"""
def isHappy(self, n):

    move = lambda n: sum(int(x) ** 2 for x in str(n))
    slow, fast = n, n
    while True:
        slow = move(slow)
        fast = move(move(fast))
        if fast == 1:
            return True
        if fast == slow:
            return False
