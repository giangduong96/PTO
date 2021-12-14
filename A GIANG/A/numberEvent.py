"""
Given an array of events where events[i] = [startDayi, endDayi].
Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei.
Notice that you can only attend one event at any time d.

Return the maximum number of events you can attend.
"""

import heapq


def maxEvent(events):
    # event [day x, day y]
    events.sort(reverse=1)      #
    heap = []
    res = day = 0
    while events or heap:
        # add the smallest event [-1] ; [[4, 4], [3, 4], [2, 2], [1, 4], [1, 1]]
        if not heap:    # add the first day
            day = events[-1][0]
        # add all events can take in day x, push day y into heap
        while events and events[-1][0] <= day:
            e = events.pop()[1]
            heapq.heappush(heap, e)

        # pop the smallest in heap, day x, add 1 for res and 1 for day
        heapq.heappop(heap)
        res += 1
        day += 1
        # pop all day in heap which smaller than day x
        while heap and heap[0] < day:
            heapq.heappop(heap)

    return res




#
events = [[1,2],[4,4],[2,2],[3,4],[1,1]]

print(maxEvent(events))
# events = [[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]
# print(maxEvent(events))
