class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # 解法：动态规划
        # 对于一座「山脉」，我们称首元素 B[0] 和尾元素 B[len(B)−1] 为「山脚」，满足题目要求
        # B[i−1]<B[i]>B[i+1] 的元素 B[i] 为「山顶」。
        # 为了找出数组 A 中最长的山脉，我们可以考虑枚举山顶，再从山顶向左右两侧扩展找到山脚。
        # 由于从左侧山脚到山顶的序列是严格单调递增的，而从山顶到右侧山脚的序列是严格单调递减的，
        # 因此我们可以使用动态规划（也可以理解为递推）的方法，计算出从任意一个元素开始，向左右两侧
        # 最多可以扩展的元素数目。
        # 先从左往右，计算每个点左侧单调递增区间的长度，用left[i]来表示A[i]向左侧最多可以扩展的元素
        # 数目，如果 A[i-1] < A[i]，那么A[i]可以向左扩展到A[i-1]，再扩展left[i]个元素，因此有：
        # left[i] = left[i-1] + 1 ---- (A[i-1] < A[i])
        # 如果 A[i-1] >= A[i]，那么A[i]无法向左扩展，同样有：
        # left[i] = 0  ---- (A[i-1] >= A[i] or i = 0)
        # 同理，我们用 right[i]表示每个点向右单调递减扩展的最大长度，那么有类似的状态转移方程为：
        # right[i] = right[i+1] + 1 ---- (A[i] > A[i+1])
        # right[i] = 0 ---- (A[i] <= A[i-1] or i = n-1)
        # 其中 n 是数组 A 的长度。在计算出所有的 left[] 以及 right[] 之后，我们就可以枚举山顶。
        # 需要注意的是，只有当left[i]和right[i]均大于0时，A[i]才能作为山顶，并且山脉的长度为left+right[i]+1。

        if not A:
            return 0

        n = len(A)
        left = [0] * n
        for i in range(1, n):
            left[i] = (left[i - 1] + 1 if A[i - 1] < A[i] else 0)

        right = [0] * n
        for i in range(n - 2, -1, -1):
            right[i] = (right[i + 1] + 1 if A[i + 1] < A[i] else 0)

        ans = 0
        for i in range(n):
            if left[i] > 0 and right[i] > 0:
                ans = max(ans, left[i] + right[i] + 1)

        return ans
