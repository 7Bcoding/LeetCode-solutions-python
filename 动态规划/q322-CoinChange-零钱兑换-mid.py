class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # 解法：动态规划
        # 我们采用自下而上的方式进行思考。仍定义 F(i) 为组成金额 i 所需最少的硬币数量，假设在计算F(i)之前，我们已经计算出F(0)−F(i−1) 的答案。 则F(i)对应的转移方程应为
        # F(i) = min { F(i-coin[j]) } + 1 (0 <= j < n-1, 0 < i <= amount)

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
