class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # 解法：深度优先搜索，标记每个访问过的点
        # 退出最上层递归则说明找到一个岛屿，岛屿数量+1

        if len(grid) == 0: return 0
        r, l = len(grid), len(grid[0])
        marked = [[False] * l for _ in range(r)]
        landnums = 0

        def dfsland(i, j):
            marked[i][j] = True
            if j < l-1:
                if grid[i][j+1] == '1' and marked[i][j+1] is False:
                    dfsland(i, j+1)
            if i < r-1:
                if grid[i+1][j] == '1' and marked[i+1][j] is False:
                    dfsland(i+1, j)
            if j > 0:
                if grid[i][j-1] == '1' and marked[i][j-1] is False:
                    dfsland(i, j-1)
            if i > 0:
                if grid[i-1][j] == '1' and marked[i-1][j] is False:
                    dfsland(i-1, j)

        for i in range(r):
            for j in range(l):
                if marked[i][j] == False and grid[i][j] == '1':
                    dfsland(i, j)
                    landnums += 1

        return landnums
