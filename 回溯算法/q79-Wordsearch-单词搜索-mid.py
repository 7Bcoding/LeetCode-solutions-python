class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        r, l = len(board), len(board[0])
        if r == 0 or word is None: return False
        flag = False

        def dfs_word(i, j, wordlist, index, count, flag, route):
            if count == len(word) and ''.join(wordlist[:]) == word:
                return True
            if i < 0 or j < 0 or i > r-1 or j > l-1:
                wordlist.append('None')
                route.append('None')
                return flag
            wordlist.append(board[i][j])
            route.append((i, j))
            if wordlist[index] == word[index]:
                if not flag and (i, j+1) not in route:
                    flag = dfs_word(i, j+1, wordlist, index+1, count+1, flag, route)
                    wordlist.pop()
                    route.pop()
                if not flag and (i+1, j) not in route:
                    flag = dfs_word(i+1, j, wordlist, index+1, count+1, flag, route)
                    wordlist.pop()
                    route.pop()
                if not flag and (i, j-1) not in route:
                    flag = dfs_word(i, j-1, wordlist, index+1, count+1, flag, route)
                    wordlist.pop()
                    route.pop()
                if not flag and (i-1, j) not in route:
                    flag = dfs_word(i-1, j, wordlist, index+1, count+1, flag, route)
                    wordlist.pop()
                    route.pop()
            else:
                return flag

            return flag

        for i in range(r):
            for j in range(l):
                flag = dfs_word(i, j, [], 0, 0, flag, [])
                if flag:
                    return True
        return flag