class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # 解法1：快速幂 + 递归
        # 「快速幂算法」的本质是分治算法。举个例子，如果我们要计算 x ^64，我们可以按照：
        # x → x^2 → x^4 → x^8 → x^16 → x^32 → x^64的顺序，从 x 开始，每次直接把上一次的结
        # 进行平方，计算 6 次就可以得到 x^64的值，而不需要对 x 乘 63 次 x。
        # 再举一个例子，如果我们要计算 x^77，我们可以按照：
        # x → x^2 → x^4 → x^9 → x^19 → x^38 → x^77
        # 在x → x^2，x^2 → x^4，x^19 → x^38 的步骤中，我们直接把上一次的结果进行平方，而在
        # x^4 → x^9，x^9 → x^19，x^38 → x^77 的步骤中，我们把上一次的结果进行平方后，还要额外乘一个x。
        # 直接从左到右进行推导看上去很困难，因为在每一步中，我们不知道在将上一次的结果平方之后，还需不需要
        # 额外乘x。但如果我们从右往左看，分治的思想就十分明显了：
        # 1. 当我们要计算 x^n 时，我们可以先递归地计算出 y = x^(n/2) ，其中⌊a⌋ 表示对 a 进行下取整；
        # 2. 根据递归计算的结果，
        #    a. 如果 n 为偶数，那么 x^n = y^2；
        #    b. 如果 n 为奇数，那么 x^n = y^2 * x
        # 3. 递归的边界为 n=0，任意数的 0 次方均为 1。
        # 由于每次递归都会使得指数减少一半，因此递归的层数为O(logn)，算法可以在很快的时间内得到结果。
        def quickMul(N):
            if N == 0:
                return 1.0
            y = quickMul(N // 2)
            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)

    def myPow(self, x, n):
        # 解法2：快速幂 + 迭代
        def quickMul(N):
            ans = 1.0
            # 贡献的初始值为 x
            x_contribute = x
            # 在对 N 进行二进制拆分的同时计算答案
            while N > 0:
                if N % 2 == 1:
                    # 如果 N 二进制表示的最低位为 1，那么需要计入贡献
                    ans *= x_contribute
                # 将贡献不断地平方
                x_contribute *= x_contribute
                # 舍弃 N 二进制表示的最低位，这样我们每次只要判断最低位即可
                N //= 2
            return ans

        return quickMul(n) if n >= 0 else 1.0 / quickMul(-n)


