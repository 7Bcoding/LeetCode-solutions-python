class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) ==0: return 0
        n, maxnum, max_l = len(nums), -1, 0
        dp = [1] * n

        for k in range(1, n):
            for i in range(k, n):
                if nums[i] <= nums[i - 1]:
                    dp[i] = dp[i - 1]
                else:
                    if nums[i] > maxnum:

                        maxnum = nums[i]
                        print(maxnum, end=' ')
                        dp[i] = dp[i-1] + 1
                    else:
                        dp[i] = dp[i - 1]

                max_l = max(max_l, dp[i])

        # print(dp)
        return max_l if max_l else 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLIS([10,9,2,5,3,4,5,5,1,5,6,7,101,6,19]))
    # print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    # # print(solution.lengthOfLIS([2, 2, 2, 3, 1]))
    # print(solution.lengthOfLIS([2, 2, 2]))
    # print(solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))