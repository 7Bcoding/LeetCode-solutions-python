class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 解法：动态规划
        # 1. 总思路：求某节点dp时，以前面每个节点为根，计算左子树和右子树的构建数量，将每个节点为
        #  根的构建数量相加，即为该节点的dp值
        # 2. 状态转移方程：
        #   * 边界情况：
        #   a. 当根左边没有节点时，该节点构建数量为 dp[i-j]，sum += dp[i-j]
        #   b. 当根右边没有节点时，该节点构建数量为 dp[j-1]，sum += dp[j-1]
        #    当根左右都有节点时，该节点构建数量为 dp[i-j]*dp[j-1]，sum += (dp[i-j] * dp[j-1])
        #  每次遍历，将经过的每个节点的dp值相加得到sum，即为当前节点的dp，直至末尾，到达最后一个
        #  节点时，dp[n]的值即为所求
        if n == 0: return 0
        dp = [1] * (n + 1)
        for i in range(1, n + 1):
            sum = 0
            for j in range(1, i + 1):
                if j == 1:
                    sum += dp[i - j]
                elif j == i:
                    sum += dp[j - 1]
                else:
                    sum += (dp[i - j] * dp[j - 1])
            dp[j] = sum
        return dp[n]
