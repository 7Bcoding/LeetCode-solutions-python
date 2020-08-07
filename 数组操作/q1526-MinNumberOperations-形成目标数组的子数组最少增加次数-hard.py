class Solution:
    def minNumberOperations(self, target):
        # 相邻的两个数，可以分为两种情况：
        # 1.左边的树比右边的数大或与右边的数相等
        # 2.左边的数比右边的数小
        re, left = 0, 0
        for n in target:
            if n>left: re += (n-left)
            left = n
        return re
