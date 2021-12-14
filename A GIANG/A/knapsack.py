# A Dynamic Programming based Python Program for 0-1 Knapsack problem
# Returns the maximum value that can be put in a knapsack of capacity W

# my version # best best best
def knapsack(total, weight, value):
    dp = [0] * (total + 1)
    dp[0] = 0

    for v in value:
        for w in range(v, total + 1):
            dp[w] = max(dp[w], v + dp[w - weight[value.index(v)]])
    return dp[total] if dp[total] != 0 else -1


val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
W = 7
print(knapsack(W, wt, val))


def knapSack(totalWeight, weightList, valueList):
    length_of_value = len(valueList)
    K = [[0 for i in range(totalWeight + 1)] for x in range(length_of_value + 1)]  # +1 because index 0

    for i in range(length_of_value + 1):
        for weight in range(totalWeight + 1):
            if i == 0 or weight == 0:  # 0 weight, mask it as 0
                K[i][weight] = 0

                # i -1 is i time since we added 0 time in
            elif weightList[i - 1] <= weight:  # check current weight vs weight on i time
                # not i but i-1 because of 0

                # select MAX value from the value above K[i] VS
                # value of value at i time + extra weight from previous calculation
                K[i][weight] = (max(valueList[i - 1] + K[i - 1][weight - weightList[i - 1]],
                                    K[i - 1][weight]))
            else:
                K[i][weight] = K[i - 1][weight]
    return K[length_of_value][totalWeight]


# Driver code
val = [1, 4, 5, 7]
wt = [1, 3, 4, 5]
W = 7

"""
  0  1  2  3  4  5  6  7
[[0, 0, 0, 0, 0, 0, 0, 0], 
 [0, 1, 1, 1, 1, 1, 1, 1], 
 [0, 1, 1, 4, 5, 5, 5, 5], 
 [0, 1, 1, 4, 5, 6, 6, 9], 
 [0, 1, 1, 4, 5, 7, 8, 9]]
"""
