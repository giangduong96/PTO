# https://leetcode.com/problems/intersection-of-two-arrays/solution/
# intersect set not intersect straight line

# naive
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            if i not in res and i in nums2:
                res.append(i)

        return res


# pro
class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)