class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        # 解法：区间DP
        # 这道题是经典的区间dp。类似石子合并问题、戳气球。
        # 切分木棍也可以想象成每次合并相邻的木棍，使得总成本最小。
        # 1. 状态dp[i][j]：
        # -- 集合：所有把[i,j]的木棍合成一根的方案
        # -- 属性：求这些方案的最小成本。
        # 2. 状态计算：
        # 设 dp[L][R] 为切割以L，R为左右端点的木棍的最小成本——
        # dp[L][R] = min(dp[L][cuts[i]] + dp[cuts[i]][R]) + R-L
        # 针对每个不同区间，L和R的值不一样，用 i , j 代替动态的区间边界值，其中i,j是截断点，
        # dp[i][j]是i到j之间截断所需最小花费，k是i到j之间所有截断点。
        # 总的Cost的大小则为：区间长度j-i + i 到某点 K 的最小Cost + K 到 j 的最小Cost，
        # 动态转移方程：dp[i][j] = min(dp[i][j], cuts[j]-cuts[i] + dp[i][k] + dp[k][j])

        cuts.sort()
        cuts.insert(0, 0)
        cuts.append(n)
        dp = [[float("inf") for j in range(len(cuts))] for i in range(len(cuts))]

        for i in range(len(cuts)):
            for j in range(len(cuts)):
                if j == i + 1:
                    dp[i][j] = 0
        for i in range(len(cuts)-1, -1, -1):
            for j in range(i+1, len(cuts)):
                if j-i > 1:
                    for k in range(i+1, j):
                        dp[i][j] = min(dp[i][j], cuts[j]-cuts[i] + dp[i][k] + dp[k][j])
        return dp[0][-1]