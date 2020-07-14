class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
      给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的连续子数组，并返回其长度。如果不存在符合条件的连续子数组，返回 0。

      示例: 

      输入: s = 7, nums = [2,3,1,2,4,3]
      输出: 2
      解释: 子数组 [4,3] 是该条件下的长度最小的连续子数组。

        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        p, minlen, sumnums = -1, n, 0
        for i in range(n):
            while p < n-1 and sumnums < s:
                p += 1
                sumnums += nums[p]
            if i == 0 and sumnums < s:
                return 0
            elif sumnums >= s:
                minlen = min(minlen, p-i+1)
            sumnums -= nums[i]
            print(minlen)

        return minlen