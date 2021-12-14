# calculate the max rectangular area under histogram with n bar
def max_rectangle_area_historgram(historgram):
    # create empty stack, the stack holds indexes of histogram[] list
    stack = list()

    max_area = 0
    index = 0

    while index < len(historgram):
        # stack[-1] is largest number in stack, histogram[stack[-1]] is value of
        # if this bar is higher than the bar on the top stack, push it to stack
        if not stack or historgram[stack[-1]] < historgram[index]:
            stack.append(index)
            index += 1

        else:
            # if this bar is lower than top of stack, then calculate the area of rectangular with stack top
            # as the smallest ( or minimum height) bar. 'i' is 'right index' for the top and element before
            # top in stack is 'left index'

            # pop the top
            top_of_stack = stack.pop()
            area = (historgram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
            max_area = max(area, max_area)

    " pop the remaining bars from stack and calculate area with every popped bar as the smallest bar"
    while stack:
        top_of_stack = stack.pop()
        area = (historgram[top_of_stack] * ((index - stack[-1] - 1) if stack else index))
        max_area = max(area, max_area)

    return max_area


# Driver Code
hist = [1,2,2]
print("Maximum area is",
      max_rectangle_area_historgram(hist))


# worse solution, divide and conquere
def calculateArea(heights, start, end):
    if start > end:
        return 0
    min_index = start
    for i in range(start, end + 1):
        if heights[min_index] > heights[i]:
            min_index = i
    return max(
        heights[min_index] * (end - start + 1),
        calculateArea(heights, start, min_index - 1),
        calculateArea(heights, min_index + 1, end),
    )


    return calculateArea(heights, 0, len(heights) - 1)

hist = [4,2,4,2]
print(calculateArea(hist, 0, 3))