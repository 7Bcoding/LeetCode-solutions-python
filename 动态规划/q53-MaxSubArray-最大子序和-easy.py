class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 解法：动态规划
        # dp[i]表示第i天的最大子序和，dp[i]为——前一天的最大子序和dp[i-1] + nums[i] 与 第i个数本身nums[i] 的最大值
        n = len(nums)
        if n == 0:
            return 0
        dp = [0] * n
        maxvalue = nums[0]
        for i in range(n):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            maxvalue = max(maxvalue, dp[i])
        return maxvalue
