class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。
        [
              [2],
             [3,4],
            [6,5,7],
           [4,1,8,3]
        ]
        自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
        """
        r = len(triangle)
        l = len(triangle[0])
        if r == 0 and l == 0: return 0
        if r == 1 and l == 1: return triangle[0][0]

        dp = [[0] * (k+1) for k in range(r)]
        dp[0][0] = triangle[0][0]
        minvalue = float('inf')

        for i in range(1, r):
            l += 1
            for j in range(l):
                if j == 0:
                    dp[i][j] = dp[i-1][j] + triangle[i][j]
                elif j == l-1:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                else:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                if i == r-1:
                    minvalue = min(minvalue, dp[i][j])
        return minvalue



