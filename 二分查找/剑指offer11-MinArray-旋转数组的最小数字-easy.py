class Solution:
    def minArray(self, numbers):
        # 我们考虑数组中的最后一个元素 x：在最小值右侧的元素，它们的值一定都小于等于 x；而在最小值左侧的元素，它们的值一定都大于等于 x。
        # 因此，我们可以根据这一条性质，通过二分查找的方法找出最小值。
        #
        # 在二分查找的每一步中，左边界为low，右边界为high，区间的中点为pivot，最小值就在该区间内。我们将中轴元素numbers[pivot]
        # 与右边界元素 numbers[high] 进行比较，可能会有以下的三种情况：
        # 1. 第一种情况是 numbers[pivot] < numbers[high]:
        #   说明 numbers[pivot] 是最小值右侧的元素，因此我们可以忽略二分查找区间的右半部分。
        # 2. 第二种情况是 numbers[pivot] > numbers[high]。
        #   说明 numbers[pivot] 是最小值左侧的元素，因此我们可以忽略二分查找区间的左半部分。
        # 3.第三种情况是 numbers[pivot]==numbers[high]。
        #   如下图所示，由于重复元素的存在，我们并不能确定numbers[pivot] 究竟在最小值的左侧还是右侧，
        #   因此我们不能莽撞地忽略某一部分的元素。我们唯一可以知道的是，由于它们的值相同，所以无论 numbers[high] 是不是最小值，都有一个它
        #   的「替代品」numbers[pivot]，因此我们可以忽略二分查找区间的右端点。
        # 当二分查找结束时，我们就得到了最小值所在的位置。

        low, high = 0, len(numbers) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if numbers[pivot] < numbers[high]:
                high = pivot
            elif numbers[pivot] > numbers[high]:
                low = pivot + 1
            else:
                high -= 1
        return numbers[low]
