class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 解法：二分查找
        # 分为2种情况：
        # 1. mid > nums[0]时，说明mid在旋转点左侧
        #   a. 若nums[0] < target < nums[mid]，则往左继续二分，r = mid - 1
        #   b. 若target > nums[mid]，则继续往右二分, l = mid + 1
        # 2. mid < nums[0]时，说明mid在旋转点右侧
        #   a. 若nums[mid] < target < nums[len(nums)-1]，则往右继续二分，l = mid + 1
        #   b. 若target < nums[mid]，则继续往左二分，r = mid - 1

        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums) - 1]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1