class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a
            b = a
            a = c
        return a