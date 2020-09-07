class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 解法：动态规划
        # dp[i][j] 表示 s 中 i 到 j 是否为回文串
        # 1. i == j，单个字符，是回文子串，dp[i][j]=True
        # 2. j-i == 1 ，两个字符，在s[i] == s[j]的情况下s[i][j]为回文子串，dp[i][j=True
        # 3. j-i > 1，dp[i+1][j-1]为True (即s[i+1][j-1]为回文子串的情况下)，
        # 同时满足s[i] == s[j]，即s[i][j]为回文子串，dp[i][j]=True
        # 当 dp[i][j] = True 时，更新最大回文子串长度
        maxl = 0
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for j in range(0, n):
            for i in range(0, j+1):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = True
                elif j - i > 1 and dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True
                if dp[i][j]:
                    maxl = max(maxl, j-i+1)
        return maxl