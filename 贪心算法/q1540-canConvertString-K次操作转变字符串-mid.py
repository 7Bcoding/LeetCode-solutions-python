class Solution(object):
    def canConvertString(self, s, t, k):
        """
        :type s: str
        :type t: str
        :type k: int
        :rtype: bool
        """
        # 哈希表 + 贪心算法
        if len(s) != len(t):
            return False

        has_oper = [0] * 26
        n = len(s)

        for i in range(n):
            a = ord(s[i])
            b = ord(t[i])
            if a != b:
                cnt = b - a if a < b else 26 - (a - b)
                check = False
                if has_oper[cnt - 1] * 26 + cnt <= k:  # 可以切换
                    has_oper[cnt - 1] += 1
                    check = True
                if not check:
                    return False
        return True