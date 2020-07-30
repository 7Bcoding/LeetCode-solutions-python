class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 解法：二分查找
        # 先通过二分查找找到第一个数，再将第一个数作为左边界，顺序查找第二个数

        low, high = 0, len(nums)-1
        if len(nums) == 0: return [-1, -1]
        left, right = 0, len(nums)-1
        while low < high:
            mid = low + (high-low) // 2
            if nums[mid] >= target:
                high = mid
            elif nums[mid] < target:
                low = mid + 1

        if nums[low] != target: return [-1, -1]
        left = low
        for i in range(left, len(nums)):
            if nums[i] > target:
                right = i-1
                break

        res = [low, right]
        return res