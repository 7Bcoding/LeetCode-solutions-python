class Solution:
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 解法1：动态规划
        # 方法一使用递归，存在大量重复计算，因此时间复杂度很高。由于存在重复子问题，因此可以使用动态规划降低时间复杂度。
        # 定义二维数组 dp，其行数和列数都等于数组的长度，dp[i][j] 表示当数组剩下的部分为下标 i 到下标 j 时，当前玩家与另一个玩家的
        # 分数之差的最大值，注意当前玩家不一定是先手。
        # 只有当 i≤j 时，数组剩下的部分才有意义，因此当 i>j 时，dp[i][j]=0。
        # 1. 当 i=j 时，只剩一个数字，当前玩家只能拿取这个数字，因此对于所有 0 ≤ i < nums.length，都有 dp[i][i]=nums[i]。
        # 2. 当 i<j 时，当前玩家可以选择 nums[i] 或 nums[j]，然后轮到另一个玩家在数组剩下的部分选取数字。在两种方案中，当前玩家会选择
        # 最优的方案，使得自己的分数最大化。因此可以得
        # 3. 到如下状态转移方程：
        # dp[i][j]=max(nums[i]−dp[i+1][j],nums[j]−dp[i][j−1])
        # 最后判断 dp[0][nums.length−1] 的值，如果大于或等于 0，则先手得分大于或等于后手得分，因此先手成为赢家，否则后手成为赢家。
        # 上述代码中使用了二维数组 dp。分析状态转移方程可以看到，dp[i][j] 的值只和 dp[i+1][j] 与 dp[i][j−1] 有关，即在计算 dp 的第
        # i 行的值时，只需要使用到 dp 的第 i 行和第 i+1 行的值，因此可以使用一维数组代替二维数组，对空间进行优化。

        length = len(nums)
        dp = [0] * length
        for i, num in enumerate(nums):
            dp[i] = num
        for i in range(length - 2, -1, -1):
            for j in range(i + 1, length):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])
        return dp[length - 1] >= 0

    # 解法2：递归
    # 为了判断哪个玩家可以获胜，需要计算一个总分，即先手得分与后手得分之差。当数组中的所有数字都被拿取时，如果总分大于或等于 0，则先手获
    # 胜，反之则后手获胜。由于每次只能从数组的任意一端拿取数字，因此可以保证数组中剩下的部分一定是连续的。假设数组当前剩下的部分为下标 start
    # 到下标 end，其中 0 ≤ start ≤ end < nums.length。
    # 如果 start = end，则只剩一个数字，当前玩家只能拿取这个数字。如果 start < end，则当前玩家可以选择 nums[start] 或 nums[end]，然后轮
    # 到另一个玩家在数组剩下的部分选取数字。这是一个递归的过程。
    # 计算总分时，需要记录当前玩家是先手还是后手，判断当前玩家的得分应该记为正还是负。当数组中剩下的数字多于 1 个时，当前玩家会选择最优的方案，
    # 使得自己的分数最大化，因此对两种方案分别计算当前玩家可以得到的分数，其中的最大值为当前玩家最多可以得到的分数。

    def PredictTheWinner(self, nums):
        def total(start: int, end: int, turn: int) -> int:
            if start == end:
                return nums[start] * turn
            scoreStart = nums[start] * turn + total(start + 1, end, -turn)
            scoreEnd = nums[end] * turn + total(start, end - 1, -turn)
            return max(scoreStart * turn, scoreEnd * turn) * turn

        return total(0, len(nums) - 1, 1) >= 0




