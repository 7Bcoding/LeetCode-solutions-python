class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        # 个人解法：DFS + 回溯
        # 每个方向都递归，使用路径标记元组存储遍历过的字符的下标，每次递归返回都弹出
        r, l = len(board), len(board[0])
        if r == 0 or word is None: return False
        flag = False

        def dfs_word(i, j, wordlist, index, flag, route):
            if index == len(word):
                return True
            if i < 0 or j < 0 or i > r-1 or j > l-1:
                wordlist.append('None')
                route.append('None')
                return flag
            wordlist.append(board[i][j])
            route.append((i, j))
            if wordlist[index] == word[index]:
                if not flag and (i, j+1) not in route:
                    flag = dfs_word(i, j+1, wordlist, index+1, flag, route)
                    wordlist.pop()
                    route.pop()
                if not flag and (i+1, j) not in route:
                    flag = dfs_word(i+1, j, wordlist, index+1, flag, route)
                    wordlist.pop()
                    route.pop()
                if not flag and (i, j-1) not in route:
                    flag = dfs_word(i, j-1, wordlist, index+1, flag, route)
                    wordlist.pop()
                    route.pop()
                if not flag and (i-1, j) not in route:
                    flag = dfs_word(i-1, j, wordlist, index+1, flag, route)
                    wordlist.pop()
                    route.pop()
            else:
                return flag

            return flag

        for i in range(r):
            for j in range(l):
                flag = dfs_word(i, j, [], 0, flag, [])
                if flag:
                    return True
        return flag

    # ------------------------------------------------------
    # 优秀解法：将每个方向的深度遍历替换成循环，而不是每个方向都递归
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def exist(self, board, word):
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 对每一个格子都从头开始搜索
                if self.__search_word(board, word, 0, i, j, marked, m, n):
                    return True
        return False

    def __search_word(self, board, word, index,
                      start_x, start_y, marked, m, n):
        # 先写递归终止条件
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]

        # 中间匹配了，再继续搜索
        if board[start_x][start_y] == word[index]:
            # 先占住这个位置，搜索不成功的话，要释放掉
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                # 注意：如果这一次 search word 成功的话，就返回
                if 0 <= new_x < m and 0 <= new_y < n and \
                        not marked[new_x][new_y] and \
                        self.__search_word(board, word,
                                           index + 1,
                                           new_x, new_y,
                                           marked, m, n):
                    return True
            marked[start_x][start_y] = False
        return False
