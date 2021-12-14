def intersectionArea(row, col, WELane, NSLane):
    """
    :type row: int
    :type col: int
    :type WELane: List[int]
    :type NSLane: List[int]
    :rtype: int
    """
    rowlane = set(WELane)
    collane = set(NSLane)

    row = 0
    col = 0

    for num in rowlane:
        if num - 1 not in rowlane:
            current_num = num
            current_streak = 1

            while current_num + 1 in rowlane:
                current_num += 1
                current_streak += 1

            row = max(row, current_streak)

    for num in collane:
        if num - 1 not in collane:
            current_num = num
            current_streak = 1

            while current_num + 1 in collane:
                current_num += 1
                current_streak += 1

            col = max(col, current_streak)

    maxlength = col * row
    return maxlength