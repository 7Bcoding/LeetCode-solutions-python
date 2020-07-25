class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 解法：动态规划
        # dp[i]表示的是前i个字符中不同的字符数
        # 以i为分隔，S(0,i)为左边的字符，S(i+1,n)为右边的字符，那么很容易得到状态方程：
        # 当加入第i个字符时——
        # 若第i个字符在前i-1个字符中，则dp[i]保持不变          --- dp[i] = dp[i-1]
        # 若第i个字符不在前i-1个字符中，则加入了一个新的不同字符 --- dp[i] = dp[i-1] + 1
        # S(0,i)中每加入一个不同的字符，S(i+1,n)就要少一个不同的字符。dp[0]时dp[0]=1，而
        # 右半部分S(1,n)总的不同字符数初始化为nums，nums即为整个字符串总的不同字符数，用set统计

        dp = [1] * len(s)
        nums = len(set(s))
        if s[0] not in s[1:]: nums -= 1
        dp[0] = 1
        count = 1 if nums == 1 else 0
        for i in range(1, len(s)-1):
            if s[i] in s[0:i]:
                dp[i] = dp[i-1]
            else:
                dp[i] = dp[i-1] + 1
            if s[i] not in s[i+1:]:
                nums -= 1
            if nums == dp[i]:
                count += 1
        return count
