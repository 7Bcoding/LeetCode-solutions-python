class Solution:
    def maxSum(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """

        # 解法：贪心算法 + 双指针
        i, j = len(nums1) - 1, len(nums2) - 1
        s1, s2 = 0, 0
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                s1 += nums1[i]
                i -= 1
            elif nums1[i] < nums2[j]:
                s2 += nums2[j]
                j -= 1
            else:
                s1 = s2 = max(s1, s2) + nums1[i]   # 每段都结算一次当前最大得分总和
                i -= 1
                j -= 1

        # 任一指针到头，继续计算完另一条路的Sum
        while i >= 0:
            s1 += nums1[i]
            i -= 1
        while j >= 0:
            s2 += nums2[j]
            j -= 1

        return max(s1, s2) % (10 ** 9 + 7)
