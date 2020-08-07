class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 算法：
        #   首先，我们初始化一个指向矩阵左下角的(row，col)指针。然后，直到找到目标并返回 true
        # （或者指针指向矩阵维度之外的(row，col) 为止，我们执行以下操作：如果当前指向的值大于目标值，
        # 则可以 “向上” 移动一行。 否则，如果当前指向的值小于目标值，则可以移动一列。不难理解为什么这
        # 样做永远不会删减正确的答案；因为行是从左到右排序的，所以我们知道当前值右侧的每个值都较大。
        #   因此，如果当前值已经大于目标值，我们知道它右边的每个值会比较大。也可以对列进行非常类似的论证，
        # 因此这种搜索方式将始终在矩阵中找到目标（如果存在）。

        r, l = len(matrix), len(matrix[0])
        if r == 0: return False

        i, j = r-1, 0
        while i >= 0 and j <= l-1:
            if matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
            else:
                return True

        return False