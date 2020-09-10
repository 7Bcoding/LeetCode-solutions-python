class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(candidates) == 0: return []
        # 在遍历的过程中记录路径，它是一个栈
        res = []
        path = []
        # 剪枝是为了提速，在本题非必需
        candidates.sort()
        cbset = set()

        def dfs_combination(candidates, begin, size, path, res, target):
            # 先写递归终止的情况
            if target == 0:
                pth = ''.join(str(path[:]))
                # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
                if pth not in cbset:
                    cbset.add(pth)
                    res.append(path[:])
                return
            for i in range(begin, size):
                residue = target - candidates[i]
                # “剪枝”操作，不必递归到下一层，并且后面的分支也不必执行
                if residue < 0:
                    break
                path.append(candidates[i])
                # 因为下一层不能比上一层还小，起始索引还从 index 开始
                dfs_combination(candidates, i+1, size, path, res, residue)
                path.pop()

        # 注意要传入 size ，在 range 中， size 取不到
        dfs_combination(candidates, 0, len(candidates), path, res, target)

        return res
