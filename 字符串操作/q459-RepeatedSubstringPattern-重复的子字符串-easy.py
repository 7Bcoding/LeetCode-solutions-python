class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 解法：暴力
        # 从字符串的头部，开始逐步往前扩大匹配子串
        # 每次子串匹配时位移的长度就是它本身的长度
        # 匹配到底则为找到，返回True，否则返回FALSE
        flag = False
        n = len(s)
        for i in range(n):
            l, r = 0, i
            if n % (i+1) != 0:
                continue
            while r+1 < n:
                print(s[l+i+1:r+i+2], end=' ')
                if s[l:r+1] == s[l+i+1:r+i+2]:
                    l = l + i + 1
                    r = r + i + 1
                    flag = True
                else:
                    flag = False
                    break
            if flag: return True
        return flag
