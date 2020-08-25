class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 解法：哈希表/散列表
        # 1. 使用set记录每次快乐数算法运算结果
        # 2. 遇到重复出现在set中的数，直接返回False
        # 3. 遇到1，返回True
        happyset = set()
        if n != 1: happyset.add(n)
        s = str(n)
        sumn = 0
        while True:
            for i in range(len(s)):
                sumn += (int(s[i]) * int(s[i]))
            if sumn in happyset: return False
            else: happyset.add(sumn)
            print(sumn, end=', ')
            if sumn == 1: return True
            s = str(sumn)
            sumn = 0
