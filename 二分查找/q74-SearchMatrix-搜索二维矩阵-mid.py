class Solution(object):

    # 解法1：抽象 BST 解法，我们可以将二维矩阵抽象成「以右上角为根的 BST」
    # 那么我们可以从根（右上角）开始搜索，如果当前的节点不等于目标值，可以按照树的搜索顺序进行：
    # 1. 当前节点「大于」目标值，搜索当前节点的「左子树」，也就是当前矩阵位置的「左方格子」，即 y--
    # 2. 当前节点「小于」目标值，搜索当前节点的「右子树」，也就是当前矩阵位置的「下方格子」，即 x++

    def searchMatrixA(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        row, column = len(matrix), len(matrix[0]) - 1
        for i in range(row):
            for j in range(column, -1, -1):
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:
                    break
        return False

    # 解法2：
    # 将二维数组拼接成一维数组，然后使用二分查找
    def searchMatrixB(self, matrix, target):
        array = []
        for i in range(1, len(matrix)):
            array.extend(matrix[i])
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            mid = (l + r) // 2
            if array[mid] == target:
                return True
            elif array[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
