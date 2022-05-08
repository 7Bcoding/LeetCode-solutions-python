class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        if len(s) == 0: return ""
        for j in range(n):
            for i in range(0, j + 1):
                if i == j:
                    dp[i][j] = True
                elif j - i == 1 and s[i] == s[j]:
                    dp[i][j] = True
                elif j - i > 0 and s[i] == s[j] and dp[i + 1][j - 1] is True:
                    dp[i][j] = True
                if dp[i][j] and j - i + 1 > len(ans):
                    ans = s[i:j + 1]
        return ans
