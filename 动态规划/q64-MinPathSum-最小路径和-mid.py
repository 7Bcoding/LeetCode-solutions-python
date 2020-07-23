class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 解法：动态规划
        # dp[i] 第i个格子的最小值
        # 每个格子的最小值为其左边的格子和上方的格子中的最小值 + 自己的值
        # 状态方程：dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        # 边界条件：第一列只能由上方格子的dp值累加，第一行只能由左边的格子的dp值累加

        if len(grid) == 0: return None
        if len(grid) ==1 and len(grid[0]) == 1: return grid[0][0]
        r, l = len(grid), len(grid[0])
        dp = [[0] * l for _ in range(r)]
        dp[0][0] = grid[0][0]

        for i in range(r):
            if i > 0:
                dp[i][0] = dp[i-1][0] + grid[i][0]
            for j in range(1, l):
                if i == 0:
                    dp[0][j] = dp[0][j-1] + grid[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        print(dp)
        return dp[r-1][l-1]