class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 解法：字符串遍历，进制转换
        # 初始化结果ans = 0，遍历时将每个字母与A做减法，因为A表示1，所以减法后需要每个数加1，计算其代表的数值num = 字母 - ‘A’ + 1
        # 因为有26个字母，所以相当于26进制，每26个数则向前进一位
        # 所以每遍历一位则 ans = ans * 26 + num
        # 以ZY为例，Z的值为26，Y的值为25，则结果为26 * 26 + 25 = 701
        # 时间复杂度：O(n)

        if not s: return 0
        n = len(s)
        res = 0
        for i in range(n):
            res += 26 ** (n - i - 1) * (ord(s[i]) - 64)
        return res
