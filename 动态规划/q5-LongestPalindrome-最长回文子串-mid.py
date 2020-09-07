class Solution:
    def longestPalindrome(self, s):
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