from collections import defaultdict


class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        # 解法：递归回溯

        def dfs(pos):
            nonlocal valid
            if pos == len(spaces):        # 表示所有空白格子已填满
                valid = True
                return

            i, j = spaces[pos]
            for digit in range(9):
                if line[i][digit] == column[j][digit] == block[i // 3][j // 3][digit] is False:
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True
                    board[i][j] = str(digit + 1)
                    dfs(pos + 1)
                    # 回溯采用更改标记的方式，对于不满足条件的数字，回溯不再通过矩阵回退删除该数的操作方式，
                    # 而是继续从剩下的数字中选择，直接覆盖该位置的数即可
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = False
                if valid:
                    return

        line = [[False] * 9 for _ in range(9)]                         # 二维矩阵标记数字在该列的存在
        column = [[False] * 9 for _ in range(9)]                       # 二维矩阵标记数字在该列的存在
        block = [[[False] * 9 for _a in range(3)] for _b in range(3)]  # 三维空间矩阵标记数字在九宫格的存在
        valid = False
        spaces = list()

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    spaces.append((i, j))         # spaces表示空白格子的下标列表
                else:
                    digit = int(board[i][j]) - 1
                    line[i][digit] = column[j][digit] = block[i // 3][j // 3][digit] = True  # 初始化已填的数字

        dfs(0)
