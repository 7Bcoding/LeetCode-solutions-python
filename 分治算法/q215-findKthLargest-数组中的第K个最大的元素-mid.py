from random import randint


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(left, right, pivot):  # pivot in [left,right]
            pivotvalue = nums[pivot]  # pivot是下标
            nums[pivot], nums[right] = nums[right], nums[pivot]
            index = left
            for i in range(left, right):
                if nums[i] > pivotvalue:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1

            nums[right], nums[index] = nums[index], nums[right]
            return index

        def select(left, right, k):
            if left == right:
                return nums[left]  # 元素非下标
            pivot = randint(left, right)
            ind = partition(left, right, pivot)
            if ind == k:
                return nums[ind]
            elif ind > k:
                return select(left, ind - 1, k)
            else:
                return select(ind + 1, right, k)

        return select(0, len(nums) - 1, k - 1)

