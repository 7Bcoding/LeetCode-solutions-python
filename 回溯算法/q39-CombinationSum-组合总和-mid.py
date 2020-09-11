class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 解法：回溯 + 剪枝
        # 根据示例 1：输入: candidates = [2,3,6,7]，target = 7。
        # 候选数组里有 2 ，如果找到了 7 - 2 = 5 的所有组合，再在之前加上 2 ，就是 7 的所有组合；
        # 同理考虑 3，如果找到了 7 - 3 = 4 的所有组合，再在之前加上 3 ，就是 7 的所有组合，依次这样找下去；
        # 1. 去重复
        # a. 在搜索的时候，需要设置搜索起点的下标 begin ，由于一个数可以使用多次，下一层的结点从这个搜索起点
        # 开始搜索；
        # b. 在搜索起点 begin 之前的数因为以前的分支搜索过了，所以一定会产生重复。
        # 2. 剪枝提速
        # a. 如果一个数位搜索起点都不能搜索到结果，那么比它还大的数肯定搜索不到结果，基于这个想法，我们可以对
        # 输入数组进行排序，以减少搜索的分支；
        # b. 排序是为了提高搜索速度，非必要；
        # c. 搜索问题一般复杂度较高，能剪枝就尽量需要剪枝。把候选数组排个序，遇到一个较大的数，如果以这个数为起
        # 点都搜索不到结果，后面的数就更搜索不到结果了。

        if len(candidates) == 0: return []
        # 在遍历的过程中记录路径，它是一个栈
        res = []
        path = []
        # 剪枝是为了提速，在本题非必需
        candidates.sort()

        def dfs_combination(candidates, begin, size, path, res, target):
            # 先写递归终止的情况
            if target == 0:
                # Python 中可变对象是引用传递，因此需要将当前 path 里的值拷贝出来
                # 或者使用 path.copy()
                res.append(path[:])
                return
            for i in range(begin, size):
                residue = target - candidates[i]
                # 剪枝操作，不必递归到下一层，并且后面的分支也不必执行
                if residue < 0:
                    break
                path.append(candidates[i])
                # 因为下一层不能比上一层还小，起始索引还从 index 开始
                dfs_combination(candidates, i, size, path, res, residue)
                path.pop()
        # 注意要传入 size ，在 range 中， size 取不到
        dfs_combination(candidates, 0, len(candidates), path, res, target)

        return res

