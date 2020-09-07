class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 解法：暴力 + 增倍除数
        # 这道题换句话说：除数能减去多少个被除数。
        # 上面就是我们简单想法，但是有个问题，当被除数为2147483648，除数为 1，必然超时？
        # 举个例子如果被除数 15，除数 3，用我们上面的方法要遍历 5 次。
        # 接下来，使用不断增倍除数 ———— 二进制移位方式 i << 1，代替乘法 i * 2
        # 比如：
        # 被除数 除数
        # 15 3
        # 12 6
        # 6 12
        # 发现除数 大于 被除数大，再重现开始
        # 6 3
        # 3 3
        # 虽然这个例子遍历次数相等，对于较大的数，可以减少时间复杂度。
        res = 0
        sign = 1 if dividend ^ divisor >= 0 else -1
        divd = abs(dividend)
        dior = abs(divisor)
        while divd >= dior:
            tmp, i = dior, 1
            while divd >= tmp:
                divd -= tmp
                res += i
                i <<= 1
                tmp <<= 1
        res = res * sign
        return min(max(-2**31, res), 2**31-1)
