class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # 解法：回溯算法 (也可以算DFS暴力搜索)

        if len(digits) == 0:
            return []
        dgdict = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                  '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
                  }
        result = []
        dgstack = []

        def dfsletter(pre, i):
            if i > len(digits): return
            for s in range(i, len(digits)):
                for dgstr in dgdict[digits[s]]:
                    dgstack.append(dgstr)
                    dfsletter(pre, s+1)
                    if len(dgstack) == len(digits):
                        result.append(''.join(dgstack))
                    dgstack.pop()
        dfsletter('', 0)
        return result


