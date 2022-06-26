class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 解法：
        # 采用归并排序，在归并排序中加入一行代码即可：
        # 当nums[i] > nums[j] 时，count += mid - i + 1
        # 即nums[j]本应在nums[i]左边，但是却在nums[i]右边，由此贡献了一个逆序对，
        # 而nums[i]后面的数都是大于nums[i]的，也都大于nums[j]对应的数，
        # 那么就贡献了mid - i + 1个逆序对，累加count，即可得到总的逆序对数量
        array = []
        self.count = 0

        temp = [0 for _ in range(len(nums))]

        def merge(nums, left, mid, right, temp):
            i = left
            j = mid + 1
            pos = 0
            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[pos] = nums[i]
                    i += 1
                else:
                    self.count += mid - i + 1  # 就是这行代码
                    temp[pos] = nums[j]
                    j += 1
                pos += 1
            while i <= mid:
                temp[pos] = nums[i]
                i += 1
                pos += 1

            while j <= right:
                temp[pos] = nums[j]
                j += 1
                pos += 1

            pos = 0
            while left <= right:
                nums[left] = temp[pos]
                left += 1
                pos += 1

        def sort(nums, left, right, temp):
            if left < right:
                mid = (left + right) // 2
                sort(nums, left, mid, temp)
                sort(nums, mid + 1, right, temp)
                merge(nums, left, mid, right, temp)

        sort(nums, 0, len(nums) - 1, temp)

        return self.count
