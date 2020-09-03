class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 解法：二分查找
        l, r = 1, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid * mid <= x:
                l = mid + 1
            else:
                r = mid - 1

        return l - 1