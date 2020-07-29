class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2  # 这种写法比 (left+right)//2 求mid的方法好，一些语言这样写可以防止溢出
            if nums[mid] > nums[mid + 1]:  # 如果满足该条件说明山峰可能是在 mid 的左侧，因为各个元素不同，所以if的条件是大于
                right = mid
            else:
                left = mid + 1
        return left