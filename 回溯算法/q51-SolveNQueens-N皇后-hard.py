class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        # 解法：回溯算法
        board = [['.'] * n for _ in range(n)]
        ans = []
        queens = []
        columns = set()

        def couldPlace(i, j):
            if j not in columns:                           # 在同一列则返回False进行回退
                for t in range(len(queens)):
                    x, y = queens[t]
                    if abs(i - x) == abs(j - y):           # 与之前放置的皇后位置进行坐标运算，在同一对角线则返回False回退
                        return False
                return True
            else:
                return False

        def addresult():
            res = []
            for i in range(len(board)):
                res.append(''.join(board[i][:]))            # 每行格式化后加入结果集
            ans.append(res)

        def placeQueen(i):
            for j in range(0, len(board[0])):
                if couldPlace(i, j):                        # 可以放置，则加入已放置的皇后列表，加入已存在的列
                    columns.add(j)
                    queens.append((i, j))
                    board[i][j] = 'Q'
                    if i == len(board) - 1:
                        addresult()
                    if not placeQueen(i + 1):               # 放置失败，回退
                        columns.remove(j)
                        queens.remove((i, j))
                        board[i][j] = '.'
                else:
                    continue
            return False

        placeQueen(0)
        return ans
