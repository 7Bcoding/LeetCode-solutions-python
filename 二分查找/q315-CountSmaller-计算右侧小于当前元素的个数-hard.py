import bisect


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        sorted_nums = []
        for i in range(len(nums) - 1, -1, -1):
            # 二分查找，Python自带的函数bisect.bisect_left和bisect_right
            # 将检索元素左(右)边的元素并排好序，并二分的查找相应插入的位置，返回该位置的下标index
            idx = bisect.bisect_left(sorted_nums, nums[i])
            ans.append(idx)
            sorted_nums.insert(idx, nums[i])
        return ans[::-1]