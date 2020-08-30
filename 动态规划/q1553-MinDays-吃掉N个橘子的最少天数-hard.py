from functools import lru_cache


class Solution(object):

    # 解法：动态规划（超时）
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [float('inf')] * (n + 1)
        dp[1] = 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + 1
            if i % 2 == 0:
                dp[i] = min(dp[i], dp[i - (i // 2)] + 1)
            if i % 3 == 0:
                dp[i] = min(dp[i], dp[i - 2 * (i // 3)] + 1)

        return dp[-1]

    # 解法：递归 + 记忆化
    def minDays(self, n):

        @lru_cache(None)
        def _mindays(n):
            if n <= 2: return n
            res = float('inf')
            if n % 3 == 0:
                res = min(res, _mindays(n - 2 * (n // 3)) + 1)
            if n % 2 == 0:
                res = min(res, _mindays(n // 2) + 1)
            # 如果不能同时被2、3整除，可能是由n-1过来，因此需要计算n-1
            if n % 2 != 0 or n % 3 != 0:
                res = min(res, _mindays(n - 1) + 1)
            return res
        return _mindays(n)



