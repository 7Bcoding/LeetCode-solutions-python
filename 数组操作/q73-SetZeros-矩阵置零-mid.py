class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # 解法：第一次遍历将有0的行和列的下标值分别存放在两个散列表中，
        # 再一次遍历将相应矩阵值置0即可
        row, col = len(matrix), len(matrix[0])
        rowset = set()
        colset = set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j] == 0:
                    rowset.add(i)
                    colset.add(j)
        while rowset:
            r = rowset.pop()
            for j in range(col):
                matrix[r][j] = 0
        while colset:
            column = colset.pop()
            for i in range(row):
                matrix[i][column] = 0