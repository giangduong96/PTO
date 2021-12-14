"""Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
"""
from collections import Counter


# DFS
def combinationSum1(array: list, target: int):
    def dfs(array, target, index, res, path):
        if target < 0:
            return
        elif target == 0:
            res.append(path)
            return

        for i in range(index, len(array)):
            # diff in this point
            if i > index and array[i] == array[i - 1]:
                continue
            dfs(array, target - array[i], i + 1, res, path + [array[i]])

    res = []
    array.sort()
    dfs(array, target, 0, res, [])
    return res


# backtracking with counter

def combinationSum2(candidates: list, target: int):
    def backtrack(comb, remain, curr, counter, result):
        if remain == 0:
            # make a deep copy of the current combination rather than keeping the reference
            result.append(list(comb))
            return

        elif remain < 0:
            return

        for next_curr in range(curr, len(counter)):
            candidate, freq = counter[next_curr]
            print("next_curr",next_curr, ",candidate" ,candidate, ",freq", freq)
            if freq <= 0:
                continue
            # add a new element to the current combination
            comb.append(candidate)
            counter[next_curr] = (candidate, freq - 1)

            # countinue the exploration with the updated combination
            backtrack(comb, remain - candidate, next_curr, counter, result)

            # backtracking the changes, so that we can try another candidate
            counter[next_curr] = (candidate, freq)
            comb.pop()

    result = []
    counter = Counter(candidates)

    counter = [(c, counter[c]) for c in counter]
    backtrack(comb=[], remain=target, curr=0, counter=counter, result=result)
    return result


candidates = [2,5,2,1,2]
target = 5

print(combinationSum1(candidates, target))