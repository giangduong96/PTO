"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

"""


def bestTime(array):
    minvalue = int("Inf")
    maxvalue = 0

    for i in range(len(array)):
        if array[i] < minvalue:
            minvalue = array[i]
        else:
            if array[i] - minvalue > maxvalue:
                maxvalue = array[i] - minvalue
    return maxvalue


# with peak valley approach
def bestTime2(array):
    valley = array[0]
    peak = array[0]
    maxprofit = 0
    i = 0
    while i < len(array) - 1:
        while i < len(array) - 1 and array[i] >= array[i + 1]:
            i += 1
        valley = array[i]
        while i < len(array) - 1 and array[i] <= array[i + 1]:
            i += 1
        peak = array[i]

        maxprofit += peak - valley
        # print(maxprofit)
    return maxprofit


print(bestTime2([7, 1, 5, 3, 6, 4]))
