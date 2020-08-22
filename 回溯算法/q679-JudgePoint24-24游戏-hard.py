class Solution:
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 解法：回溯算法
        #   一共有 4 个数和 3 个运算操作，因此可能性非常有限。一共有多少种可能性呢？
        #   首先从 4 个数字中有序地选出 2 个数字，共有 4  3=124×3=12 种选法，并选择加、减、乘、除
        #   4 种运算操作之一，用得到的结果取代选出的 2 个数字，剩下 3 个数字。
        # 然后在剩下的 3 个数字中有序地选出 2 个数字，共有 3  2=63×2=6 种选法，并选择 4 种运算操
        # 作之一，用得到的结果取代选出的 2 个数字，剩下 2 个数字。最后剩下 2 个数字，有 2 种不同的顺序，
        # 并选择 4 种运算操作之一。
        #   因此，一共有 12 × 4 × 6 × 4 × 2 × 4 = 9216 种不同的可能性。可以通过回溯的方法遍历所有不同
        # 的可能性。具体做法是，使用一个列表存储目前的全部数字，每次从列表中选出 2 个数字，再选择一种运算操
        # 作，用计算得到的结果取代选出的 2 个数字，这样列表中的数字就减少 1 个。重复上述步骤，直到列表中只
        # 剩下 1 个数字，这个数字就是一种可能性的结果，如果结果等于 2424，则说明可以通过运算得到 2424。如
        # 果所有的可能性的结果都不等于 2424，则说明无法通过运算得到 2424。
        # 3. 实现时，有一些细节需要注意。
        # a. 除法运算为实数除法，因此结果为浮点数，列表中存储的数字也都是浮点数。在判断结果是否等于 2424 时应考虑精
        # 度误差，这道题中，误差小于10^{-6}可以认为是相等。
        # b. 进行除法运算时，除数不能为 00，如果遇到除数为 00 的情
        # 况，则这种可能性可以直接排除。由于列表中存储的数字是浮点数，因此判断除数是否为 00 时应考虑精度误差，这道
        # 题中，当一个数字的绝对值小于 10^{-6}时，可以认为该数字等于 0。
        # 4. 还有一个可以优化的点：
        # 加法和乘法都满足交换律，因此如果选择的运算操作是加法或乘法，则对于选出的 2 个数字
        # 不需要考虑不同的顺序，在遇到第二种顺序时可以不进行运算，直接跳过。
        #
        TARGET = 24
        EPSILON = 1e-6
        ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3

        def solve(nums):
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == ADD:
                                newNums.append(x + y)
                            elif k == MULTIPLY:
                                newNums.append(x * y)
                            elif k == SUBTRACT:
                                newNums.append(x - y)
                            elif k == DIVIDE:
                                if abs(y) < EPSILON:
                                    continue
                                newNums.append(x / y)
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False

        return solve(nums)