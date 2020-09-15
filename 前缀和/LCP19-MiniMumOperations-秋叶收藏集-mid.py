class Solution(object):
    def minimumOperations(self, leaves):
        """
        :type leaves: str
        :rtype: int
        """
        # 解法：数组前缀和
        # 用 sum[x] 表示 [0, x) 区间内红叶数量. 假设整理后红叶的区间为 [0, i) 和 [j, n), 那么黄叶区间为 [i, j).
        # 对于左右两个区间, 操作次数为区间长度减去红叶的数量, 对于中间的区间, 操作次数就是红叶的数量.
        # 需要操作的总次数为 (i - sum[i]) + (n - j - sum[n] + sum[j]) + (sum[j] - sum[i]), 整理后得到
        # n - sum[n] + (i - 2 * sum[i]) - (j - 2 * sum[j]), 约束条件为 0 < i < j < n. 为了让操作数最少,
        # 我们希望 j 确定时 i - 2 * sum[i] 最小。用 minvalue[x] 记录 [1, x] 区间内的 i - 2 * sum[i] 的最小值,
        # 将 j 从 n - 1 遍历到 2, min[j - 1]即为当前最小的 i - 2 * sum[i].

        n = len(leaves)
        arr = list(leaves)
        sum = [0] * (n+1)
        for i in range(n):
            sum[i + 1] = sum[i] + (arr[i] == 'r')
        minvalue = [0] * (n+1)
        currentMin = float('inf')
        for i in range(n-1):
            currentMin = min(currentMin, i - 2 * sum[i])
            minvalue[i] = currentMin

        result = float('inf')
        for j in range(n-1, 1, -1):
            result = min(result, n - sum[n] + minvalue[j - 1] - j + 2 * sum[j])
        return result

