"""
use Recursive: N * O(2^N), Space: N * O(2^N)
"""


def subsets(array):
    output = [[]]

    for num in array:
        output += [current + [num] for current in output]
        #print(output)
        # output.append( [current + [num] for current in output])

    return output


"""
backtracking N * O(2^N), space = O(N)
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
"""


def subsets2(array):
    def backtracking(first=0, current=[]):
        # if the combination is done
        if len(current) == k:
            output.append(current[:])
            return
        for i in range(first, n):
            # add array[i] into the current combination
            current.append(array[i])
            backtracking(i + 1, current)
            current.pop()

    output = []
    n = len(array)
    for k in range(n + 1):
        backtracking()
    return output


def subsets3(array):  # another way to implement backtracking search
    res = []
    subset = []

    def dfs(i):
        if i >= len(array):
            res.append(subset.copy())
            return

        # decision to include nums[i]
        subset.append(array[i])
        dfs(i + 1)

        # decision NOT include num[i]
        subset.pop()
        dfs(i + 1)

    dfs(0)
    return res


def subset4(array):
    n = len(array)
    output = []

    for i in range(2 ** n, 2 ** (n + 1)):
        # generate bitmask from 0...00 to 1..11
        bitmask = bin(i)[3:]

        # append subset corresponding to that bitmask
        output.append([array[j] for j in range(n) if bitmask[j] == '1'])
    return output


print(subsets([4,3,2,5,6,]))
