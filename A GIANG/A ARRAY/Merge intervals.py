# https://leetcode.com/problems/merge-intervals/

def mergeInterval(intervals):
    intervals.sort(key=lambda x: x[0])
    merge = []
    for interval in intervals:
        # if the list of merged intervals is empty or if the current intervals does not overlap with the previous
        if not merge or merge[-1][1] < interval[0]:
            print(merge, interval)
            merge.append(interval)
        else:
            # otherwise, there is overlap, so we merge the current and previous
            print("else", merge, interval)
            merge[-1][1] = max(merge[-1][1], interval[1])
    return merge

print(mergeInterval([[0,2],[0,1],[0, 2],[1,9], [2,5],[10,11]]))