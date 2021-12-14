"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.
"""


# brute force
def findDiagonalOrder(matrix: list):
    if not matrix or not matrix[0]:
        return []

    N, M = len(matrix), len(matrix[0])
    result, intermediate = [], []
    print(N, M)
    for d in range(M + N - 1):
        # print(intermediate, "in")
        intermediate.clear()

        # r, c = 0 if d < M else d - M + 1, d if d < M else M - 1
        if d < M:
            r = 0
            c = d
        else:
            r = d - M + 1
            c = M - 1

        print("r, c", r, c, d)
        while r < N and c > -1:
            intermediate.append(matrix[r][c])
            r += 1
            c -= 1

        if d % 2 == 0:
            result.extend(intermediate[::-1])
        else:
            result.extend(intermediate)
    return result


mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(findDiagonalOrder(mat))




