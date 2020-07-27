class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        subset = []
        # 解法：回溯算法
        # q46-全排列 类似，不同之处：为了防止重复，加了index，每次递归从i+1处开始遍历

        def dfssubset(index, subset, k):
            if len(subset) == k:
                res.append(subset[:])
                return
            for i in range(index, len(nums)):
                if nums[i] not in subset:
                    subset.append(nums[i])
                    dfssubset(i+1, subset, k)
                    subset.pop()

        for k in range(len(nums)+1):
            dfssubset(0, subset, k)

        return res

