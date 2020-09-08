class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        # 解法：动态规划
        # 两个字符串的动态规划问题，套路是通用的。
        # 第一步，dp数组的含义。比如说对于字符串 s1 和 s2，一般来说都要构造一个DP table
        # 索引是从 1 开始的，其中，dp[i][j] 的含义是：对于 s1[1..i] 和 s2[1..j]，它们的 LCS 长度是 dp[i][j]。
        #
        # 第二步，定义 base case。
        # 让索引为 0 的行和列表示空串，dp[0][..] 和 dp[..][0] 都应该初始化为 0，这就是 base case。
        # 比如说，按照刚才 dp 数组的定义，dp[0][3]=0 的含义是：对于字符串 "" 和 "bab"，其 LCS 的长度为 0。
        # 因为有一个字符串是空串，它们的最长公共子序列的长度显然应该是 0。
        #
        # 第三步，找状态转移方程。
        # 1.当str1[i] == str2[j]时，dp[i][j] = 1 + dp[i-1][j-1]————匹配到一个新的字符，即str1前一个字符在前一个子串
        # 中的匹配数量+1，举例，str1 'ac'在str2 'babc'中匹配数量为2，其实是str1的'a' 在 'bab'中匹配数量+ 1（'c'在'c'中匹配数量）
        # 2.当str1[i] != str2[j]时，dp[i][j] = max(dp[i-1][j], dp[i][j-1])————延续之前的状态中的最大长度。举例：ac在babcd中
        # 匹配数量为2，延续之前 'ac'在'babc' 和 'a'在'babcd' 的匹配数量中的最大值

        m, n = len(text1), len(text2)
        # 构建 DP table 和 base case
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 进行状态转移
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    # 找到一个 lcs 中的字符
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[-1][-1]
