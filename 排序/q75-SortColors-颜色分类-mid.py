class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 个人解法：遇到0弹出，插入到最前面，遇到2，弹出，插入到最后面，遇到1，弹出，
        # 插入到最后一个0的后面一位，需要一个zero来标记最后一个0的位置
        zero = 0
        for i in range(len(nums)):
            if nums[i] == 2:
                nums.pop(i)
                nums.append(2)
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                zero += 1
            if nums[i] == 1:
                nums.pop(i)
                nums.insert(zero, 1)
        return nums

    # 官方解法: 快速排序思想
    # 三指针，两个慢指针，代表0和2，分别从前往后和从后往前遍历，一个快指针，从前往后遍历
    # p0为0和1的分界线，p2为1和2的分界线，curr为快指针
    # 1. 遇到0时，p0与curr交换，p0 + 1，curr + 1 (因为从前面换上来的一定是1，所以curr往后走一位)
    # 2. 遇到1时，往前走一位
    # 3. 遇到2时，p2与curr交换，p2 - 1，curr不动 (因为从后面换上来的可能是1可能是0，需要再走一轮循环判断)

    def sortColors(self, nums):
        '''
        荷兰三色旗问题解
        '''
        # 对于所有 idx < p0 : nums[idx < p0] = 0
        # curr是当前考虑元素的下标
        p0 = curr = 0
        # 对于所有 idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
