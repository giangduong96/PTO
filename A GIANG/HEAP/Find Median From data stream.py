"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0


Constraints:

-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.


Follow up:

If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
"""


# brute force
# time O(n log n)
import heapq


def medianFind():
    result = []

    def addNum(num):
        result.append(num)

    def findMedian():
        result.sort()
        n = len(result)
        if n % 2 == 0:
            return (result[(n/2) -1] + result[n/2]) /2
        else:
            result[n//2]


# median in max of its left and min of its right [ ....highest][ median][lowest....]
# 2 heaps - reason for 2 heaps because min heap just holds minimum value and not guarantee for max
# otherwise, max heap just hold max value not guarantee min heap
# heapify cost O (log n), 5* heapify  + O(1) == O(log n), 5 bc at least have 2 number,
# even array size doesnt have median, odd has
# constrain: array has at least 1 element
# how great neg value is how small it is

def twoheap():
    maxheap = []    # store larger numbers part, invert min heap why need -
    minheap = []    # store lower number part, max minheap is small number before median

    def addNum(num):
        # heapq.heappush(maxheap, -num)
        # heapq.heappush(minheap, -heapq.heappop(maxheap))
        # if len(minheap) > len(maxheap):
        #     heapq.heappush(maxheap, -heapq.heappop(minheap))

        if len(maxheap) == len(minheap):
            heapq.heappush(maxheap, -heapq.heappushpop(minheap, -num))
            print("a", maxheap, minheap)
        else:
            heapq.heappush(minheap, -heapq.heappushpop(maxheap, num))
            print("b", maxheap, minheap)

    def findMedian():
        if len(maxheap) > len(minheap):
            return maxheap[0]
        return (maxheap[0] - minheap[0]) / 2

    addNum(41)
    addNum(35)
    addNum(62)
    addNum(4)
    addNum(97)
    addNum(109)
    print(findMedian())

twoheap()