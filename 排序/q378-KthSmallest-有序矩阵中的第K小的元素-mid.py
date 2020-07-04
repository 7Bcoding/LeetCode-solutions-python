import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
        示例：
        matrix = [
        [ 1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]
        ],  k = 8,
        返回 13。

        """
        # 解法一：最简单的做法，转化成一维数组后直接排序，选择第K个即可
        # a = sorted(sum(matrix, []))
        # return a[k-1]

        # 解法二：归并排序
        # 这个矩阵的每一行均为一个有序数组。问题即转化为从这 n 个有序数组中找第 k 大的数，可以想到利用归并排序的做法，归并到第 k 个数即可停止。
        # 一般归并排序是两个数组归并，而本题是 n 个数组归并，所以需要用小根堆维护，以优化时间复杂度。
        # 时间复杂度：O(klogn)，归并 k 次，每次堆中插入和弹出的操作时间复杂度均为log(n)。
        # 空间复杂度：O(n)，堆的大小始终为 n。

        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))

        return heapq.heappop(pq)[0]

