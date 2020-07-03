class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        dp = {1: 1, 2: 2}
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
