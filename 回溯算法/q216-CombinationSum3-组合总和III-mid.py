class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        array = [0] * 10
        for i in range(1, 10):
            array[i] = i
        res = []
        # 在遍历的过程中记录路径，它是一个栈
        path = []

        def dfs_combination(array, begin, size, path, res, n):
            # 递归终止的情况：组合数组的和为n且长度达到k
            if n == 0 and len(path) == k:
                res.append(path[:])
                return
            elif len(path) > k:
                return
            for i in range(begin, size):
                residue = n - array[i]
                # 剪枝操作，不必递归到下一层，并且后面的分支也不必执行
                if residue < 0:
                    break
                path.append(array[i])
                # 因为下一层不能比上一层还小，起始索引还从 index 开始
                dfs_combination(array, i+1, size, path, res, residue)
                path.pop()
        # 注意要传入 size ，在 range 中， size 取不到
        dfs_combination(array, 1, len(array), path, res, n)

        return res

