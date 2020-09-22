class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 解法1：回溯算法--位置交换
        # 以[1, 2, 3]为例子，按照下面的树回溯出整个全排列：
        # [|1, 2, 3] -> [1|, 2, 3]
        # [1|, 2, 3] -> [1, 2|, 3], [2, 1|, 3]
        # [1, 2|, 3] -> [1, 2, 3|], [3, 2, 1|], [1, 3, 2|]
        # [2, 1|, 3] -> [2, 1, 3|], [3, 1, 2|], [2, 3, 1|]
        # 以[1, 2|, 3] -> [1, 2, 3|], [3, 2, 1|], [1, 3, 2|]为例，'|'
        # 往后移动一位，得到[1, 2, 3|]；[1, 2, 3|]中的3和1位置交换，得到[3, 2, 1|]；
        # [1, 2, 3|]中的3和2交换位置，得到[1, 3, 2|]。
        # 解法2：回溯算法--记忆数组记录下标(代码略)
        # 通过数组下标index加入栈中来区分已经填写过的数，每次回溯从栈中弹出先前添加过的下标，
        # 相比起全排列I比不同之处就是除了填充序列的数组memory，还需要多一个记录下标的list

        def backtrack(current_len=0):
            if current_len == n:
                res.append(nums[:])
                return
            backtrack(current_len + 1)
            for i in range(0, current_len):
                if nums[i] == nums[current_len]:
                    return
                nums[current_len], nums[i] = nums[i], nums[current_len]
                backtrack(current_len + 1)
                nums[current_len], nums[i] = nums[i], nums[current_len]

        nums.sort()
        n = len(nums)
        res = []
        backtrack()
        return res