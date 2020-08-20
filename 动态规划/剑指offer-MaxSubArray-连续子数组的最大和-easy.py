class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 解法：动态规划
        # 1. 状态定义：dp[i]表示 以nums[i]为结尾的最大连续子数组和
        # 2. 转移方程：
        # 若 dp[i−1] ≤ 0 ，说明dp[i-1]对dp[i]产生负贡献，即dp[i−1]+nums[i] 还不如nums[i]本身大。
        # 当 dp[i−1] > 0 时：执行 dp[i] = dp[i−1] + nums[i] ；
        # 当 dp[i−1] ≤ 0 时：执行 dp[i] = nums[i] ；
        # 3. 初始状态： dp[0] = nums[0]，即以nums[0]结尾的连续子数组最大和为nums[0] 。
        # 4. 返回值： 返回 dpdp 列表中的最大值，代表全局最大值。

        dp = [float('-inf')] * len(nums)
        dp[0], maxsub = nums[0], 0
        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
            maxsub = max(maxsub, dp[i])
        return maxsub


