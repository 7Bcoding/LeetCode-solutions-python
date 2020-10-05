class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # 解法：双指针
        if len(nums) < 4: return []
        nums.sort()
        result = []

        for idx in range(len(nums) - 3):
            # 这是加速项目，如果当前位置的数字+剩余位置数位的下一个数的倍数>target，则分析当前位置无意义，直接跳出循环
            if nums[idx] + nums[idx + 1] * 3 > target: break
            # 如果当前的索引 idx > 1，就要走到一个不重复数字的索引上去
            if idx > 0 and nums[idx] == nums[idx - 1]: continue
            # 这是加速项目，如果当前位置的数字+剩余位置数位的最后（大）数的倍数<target，则分析当前位置无意义，继续找下一个索引
            if nums[idx] + nums[-1] * 3 < target: continue

            for i in range(idx + 1, len(nums) - 2):
                # 同样的加速项目
                if nums[idx] + nums[i] + nums[i + 1] * 2 > target: break
                if nums[idx] + nums[i] + nums[-1] * 2 < target: continue
                if i > idx + 1 and nums[i] == nums[i - 1]: continue
                # 定位好了两个数，在剩下的区间用双指针找两数之和
                j, k = i + 1, len(nums) - 1
                while j < k:
                    s = nums[idx] + nums[i] + nums[j] + nums[k]
                    if s > target:
                        k -= 1
                    elif s < target:
                        j += 1
                    else:
                        result.append([nums[idx], nums[i], nums[j], nums[k]])
                        while j < k and nums[j] == nums[j + 1]: j += 1
                        while j < k and nums[k] == nums[k - 1]: k -= 1
                        j += 1
                        k -= 1
        return result
