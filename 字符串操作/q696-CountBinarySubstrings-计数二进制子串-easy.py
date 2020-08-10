class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 解法：按字符分组
        # 我们可以将字符串 ss 按照 00 和 11 的连续段分组，存在 \rm countscounts 数组中，例如 s = 00111011s=00111011，
        # 可以得到这样的 \rm countscounts 数组：{\rm counts} = \{2, 3, 1, 2\}counts={2,3,1,2}。
        #
        # 这里 counts 数组中两个相邻的数一定代表的是两种不同的字符。假设 counts 数组中两个相邻的数字
        # 为u或者v，它们对应着u个0和v个1，或者u个1和v个0，它们能组成的满足条件的子串数目为min{u,v}，即一对相邻的数字对答案的贡献。

        count = [1]
        j = 0
        for i in range(1, len(s)):           # 统计连续的频数
            if s[i] == s[i-1]:
                count[j] += 1
            else:
                count.append(1)
                j += 1
        res = 0
        for k in range(1, len(count)):
            res += min(count[k], count[k-1]) # 取相邻频数的最小值
        return res
