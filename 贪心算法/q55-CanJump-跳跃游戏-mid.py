class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_i = 0  # 初始化当前能到达最远的位置
        n = len(nums)-1
        for i in range(n):  # i为当前位置，jump是当前位置的跳数
            if i <= max_i < i + nums[i]:  # 如果当前位置能到达，并且当前位置+跳数>最远位置
                max_i = i + nums[i]  # 更新最远能到达位置
                if max_i > n:
                    return True
        return max_i >= i
