# bottom up method with normal table
def longestCommonSubsequence(text1, text2):  # text1 is row, text2 is col
    dp_grid = [[0] * (len(text1) + 1) for col in range(len(text2) + 1)]

    for row in range(len(text2) + 1):  # note: text2 is col but will put it to keep track each row
        for col in range(len(text1) + 1):  # note: text1 is row but will put it to keep track each col
            # if there is no letter, also a base case
            if row == 0 or col == 0:
                dp_grid[row][col] = 0
            elif text1[col - 1] == text2[row - 1]:  # -1 because we use index 0 for no letter
                # if there is a match character, increase 1 from previous dp
                dp_grid[row][col] = 1 + dp_grid[row - 1][col - 1]
            else:
                # if there is no match, we choose MAX ( previous row-1 or col-1)
                dp_grid[row][col] = max(dp_grid[row][col-1], dp_grid[row-1][col])

    return dp_grid[len(text2)][len(text1)]

### leetcode reverse string, same as above, just reverse table
def longestCommonSubsequence(text1, text2):
    # make a grid of O's with len(text2) + 1 columns and len(text1) + 1 rows
    dp_grid = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]

    # iterate up each column, starting from the last one
    for col in reversed(range(len(text2))):
        for row in reversed(range(len(text1))):
            # if characters are same
            if text2[col] == text1[row]:
                dp_grid[row][col] = 1 + dp_grid[row + 1][col + 1]  # dp_grid[row +1][col +1] because reversed
            # otherwise it must be different
            else:
                dp_grid[row][col] = max(dp_grid[row + 1][col], dp_grid[row][col + 1])

    return dp_grid[0][0]



# instead of 2D array we can use 2 array
def longestCommonSubsequenceSaveSpace(text1, text2):
    # if text1 doesnt reference the shortest string, swap them
    if len(text2) < len(text1):
        text1, text2 = text2, text1

    # dp on length of shorter text
    previous = [0] * (len(text1) + 1)

    for col in reversed(range(len(text2))):
        current = [0] * len(text1 + 1)
        for row in reversed(range(len(text1))):
            if text2[col] == text1[row]:
                current[row] = 1 + previous[row + 1]
            else:
                current[row] = max(previous[row], current[row + 1])
        previous = current
    return previous[0]




text1 = 'actgattag'
text2 = 'gtgtgatcg'

print(longestCommonSubsequence(text1, text2))
