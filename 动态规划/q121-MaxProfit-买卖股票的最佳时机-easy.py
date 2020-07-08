class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 动态规划一般分为一维、二维、多维（使用状态压缩），对应形式为 dp(i)、dp(i)(j)、二进制dp(i)(j)。
        # 1. 动态规划做题步骤：
        #   a. 明确 dp(i)应该表示什么（二维情况：dp(i)(j)）；
        #   b. 根据 dp(i) 和 dp(i-1)的关系得出状态转移方程；
        #   c. 确定初始条件，如 dp(0)dp(0)。
        # 2. 本题思路：
        #   dp[i]表示第i天的最大利润，则 dp[i]= max(dp[i-1], prices[i]-minprice)
        #   即拿今天的最大利润和之前的最大利润作比较，更大的值更新为当前最大利润

        n = len(prices)
        if n == 0:
            return 0
        # 只遍历一次，dp表示从第1到第n天的最大利润数组
        dp = [0] * n
        minprice = prices[0]
        for i in range(n):
            minprice = min(prices[i], minprice)
            dp[i] = max(dp[i-1], prices[i]-minprice)
        return dp[-1]