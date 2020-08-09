class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 贪心 + 前缀和
        # 前缀和减去目标值出现在set中，说明存在满足条件的区间——
        # 如果差值0说明是整个区间满足，如果差值不是0，说明从差值点到当前点的区间满足
        # 一旦满足再将初始化前缀和与set

        s, sums, ans = {0}, 0, 0
        for num in nums:
            sums += num
            if sums - target in s:
                ans += 1
                s, sums = {0}, 0
            else:
                s.add(sums)
        return ans
