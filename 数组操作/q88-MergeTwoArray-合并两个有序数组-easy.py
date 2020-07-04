class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1 += nums2
            for k in range(n):
                nums1.pop(0)
            return
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums2[i] <= nums1[j] or (nums1[j] == 0 and j >= len(nums1)-n):
                    nums1.insert(j, nums2[i])
                    nums1.pop()
                    n -= 1
                    break

