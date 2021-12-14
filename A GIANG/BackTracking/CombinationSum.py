"""
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""


# backtracking with array element can be used again
# T: O( N ^ (t/m) +1 ) where N is len array, t is target value, m is min array
def combinationSumI(array, target):
    result = []

    def backtrack(remain, combination, start):
        if remain == 0:
            # make a deep copy of the current combination
            result.append(list(combination))
            return
        elif remain < 0:
            # exceed the scope, stop exploration
            return

        for i in range(start, len(array)):
            # add number into combination
            combination.append(array[i])
            # give the current number another chance, rather than moving on

            backtrack(remain - array[i], combination, i)  # i in function backtrack to make sure we dont have
            # duplicate

            # backtrack, remove the number of the combination
            combination.pop()

    backtrack(target, [], 0)

    return result


from collections import Counter


# backtracking with element CANNOT be used again
# backtracking with counter
def combinationSumII(array, target):
    def backtracking(combination, remain, current, counter, results):
        if remain == 0:
            # deep copy of current combination rather than keep the reference
            results.append(list(combination))
            return
        elif remain < 0:
            return

        for next_current in range(current, len(counter)):
            candidate, freq = counter[next_current]
            if freq <= 0:
                continue

            # add new element to the current combination
            combination.append(candidate)
            counter[next_current] = (candidate, freq - 1)
            # continue the exploration with the updated combination
            backtracking(combination, remain - candidate, next_current, counter, results)  # note: next_current pass in
            # function, not current because we need avoid duplicate

            # backtracking the changes, so we can try another candidate
            counter[next_current] = (candidate, freq)
            combination.pop()

    result = []

    counter = Counter(array)
    # convert counter table to a list of (num, count)
    counter = [(num, counter[num]) for num in counter]

    # first root tree is []
    backtracking(combination=[], remain=target, current=0, counter=counter, results=result)

    return result


arr = [1, 2, 4, 2, 3, 2]

print(combinationSumI(arr, 10))

# backtracking to find fixex length
"""
Find all valid combinations of k numbers that sum up to n such that the following conditions are true:

Only numbers 1 through 9 are used. [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Each number is used at most once.
Return a list of all possible valid combinations. The list must not contain the same combination twice, 
and the combinations may be returned in any order."""


def combinationSumIII(k, target):
    result = []

    def backtracking(combination, remain, next_stage):
        # deep copy of current combination
        if remain == 0 and len(combination) == k:
            result.append(list(combination))
            return
        elif remain < 0 or len(combination) == k:
            # exceed the scope, no need to explore further
            return

        # iterate through the reduced list of candidates # Only numbers 1 through 9 are used
        for i in range(next_stage, 9):
            combination.append(i + 1)

            backtracking(combination, remain - i - 1, i + 1)  # note: i + 1 mean we dont use element again
            combination.pop()

    backtracking(combination=[], remain=target, next_stage=0)

    return result


print(combinationSumIII(3, 8))
