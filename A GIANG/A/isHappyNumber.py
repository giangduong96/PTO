# https://leetcode.com/problems/happy-number/solution/


# cycle detection
# O(log n) Space O(1)
def isHappy(number):
    def nextNumber(number):
        sumTotal = 0
        while number > 0:
            number, digit = divmod(number, 10)
            sumTotal += digit * digit
        return sumTotal

    slow = number
    fast = nextNumber(number)
    while fast != 1 and slow != fast:
        slow = nextNumber(slow)
        fast = nextNumber(nextNumber(fast))

    return fast == 1

print(isHappy(7))