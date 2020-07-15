class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        minv = float('inf')
        mid = float('inf')
        for i in range(len(nums)):
            if nums[i] <= minv:
                minv = nums[i]
            elif nums[i] <= mid:
                mid = nums[i]
            else:
                return True
        return False