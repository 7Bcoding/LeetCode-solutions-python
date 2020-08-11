class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 解法：深度优先遍历
        # 本题给定的矩阵中有三种元素：
        # 1. 字母 X；
        # 2. 被字母 X 包围的字母 O；
        # 3. 没有被字母 X 包围的字母 O。
        # 本题要求将所有被字母 X 包围的字母 O都变为字母 X ，但很难判断哪些 O 是被包围的，哪些 O 不是被包围的。
        # 任何边界上的 O 都不会被填充为 X。 我们可以想到，所有的不被包围的 O 都直接或间接
        # 与边界上的 O 相连。我们可以利用这个性质判断 O 是否在边界上，具体地说：
        # 1.对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母 O；
        # 2. 最后我们遍历这个矩阵，对于每一个字母：
        #  a. 如果该字母被标记过，则该字母为没有被字母 X 包围的字母 O，我们将其还原为字母 O；
        #  b. 如果该字母没有被标记过，则该字母为被字母 X 包围的字母 O，我们将其修改为字母 X。

        if not board:
            return

        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return

            board[x][y] = "A"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
