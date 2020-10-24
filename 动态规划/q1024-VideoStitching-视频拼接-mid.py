class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        # 解法：动态规划
        # 比较容易想到的方法是动态规划，我们令 dp[j] 表示将区间 [0 , j) 覆盖所需的最少子区间的数量。
        # 由于我们希望子区间的数目尽可能少，因此可以将所有的初始值设为一个大整数，并将 dp[0]（即空区间）的初始值设为 0。
        # 我们可以枚举所有的子区间来依次计算出所有的 dp值。我们首先枚举 i ，同时对于任意一个子区间 [aj , bj),
        # 若其满足 aj < i <= bj，那么它就可以覆盖区间 [0 , i) 的后半部分，而前半部分则可以用 dp[aj]对应的最优方法进行
        # 覆盖，因此我们可以用 dp[aj] + 1 来更新 dp[i]。
        # 状态转移方程如下：
        # dp[i] = min{ dp[aj] } + 1 (aj < i <= bj) 最终的答案即为 dp[T]。

        dp = [float("inf")] * T
        for i in range(1, T + 1):
            for aj, bj in clips:
                if aj < i <= bj:
                    dp[i] = min(dp[i], dp[aj] + 1)

        return -1 if dp[T] == float("inf") else dp[T]

