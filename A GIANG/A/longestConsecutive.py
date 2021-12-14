"""
HashSet and Intelligent Sequence Building
Intuition

It turns out that our initial brute force solution was on the right track,
but missing a few optimizations necessary to reach O(n)O(n) time complexity.

Algorithm

This optimized algorithm contains only two changes from the brute force approach:
the numbers are stored in a HashSet (or Set, in Python) to allow O(1)O(1) lookups,
and we only attempt to build sequences from numbers that are not already part of a longer sequence.
This is accomplished by first ensuring that the number that would immediately precede
the current number in a sequence is not present, as that number would necessarily be part of a longer sequence.
"""
# Note: set is not sorted,

def longestConsecutive(nums):
    longest_streak = 0
    num_set = set(nums)
    # print(num_set)
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


print(longestConsecutive([3, 4, -1, 0, 6, 2, 3]))
