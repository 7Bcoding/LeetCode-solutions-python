class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 解法：回溯算法
        # 用一个记忆数组memory，深度遍历时，记录已经添加的元素，到递归的下一层，
        # 从头遍历nums时，就跳过memory中的元素，添加不在记忆数组里的元素。
        # 递归边界条件：当记忆数组长度达到nums时，加入res结果集，然后返回上一层
        # 递归返回时，弹出之前一层添加的元素
        result = []
        array = []

        def backtrack():
            if len(array) == len(nums):
                result.append(array[:])
                return
            for i in range(len(nums)):
                if nums[i] not in array:
                    array.append(nums[i])
                    backtrack()
                    array.pop()

        backtrack()
        return result

