# https://leetcode.com/problems/missing-ranges/
# time O(N), space O(1)
def missingRange(array, lower, higher):
    def formatRange(lower, higher):
        if lower == higher:
            return str(lower)
        return str(lower) + "->" + str(higher)

    result = []
    prev = lower - 1
    for i in range(len(array) + 1):
        if i < len(array):
            current = array[i]
        else:
            current = higher

        if prev + 1 <= current - 1:
            result.append(formatRange(prev + 1, current - 1))
        prev = current
    return result


nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
print(missingRange(nums, lower, upper))
