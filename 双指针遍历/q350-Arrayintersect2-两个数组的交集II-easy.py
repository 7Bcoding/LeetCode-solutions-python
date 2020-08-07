class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        给定两个数组，编写一个函数来计算它们的交集。
        示例 1: 输入: nums1 = [1,2,2,1], nums2 = [2,2]       输出: [2,2]
        示例 2: 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]   输出: [4,9]
        """
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        print(nums1)
        print(nums2)
        result = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result
