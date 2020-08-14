class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 解法：双指针
        # 在初始时，左右指针分别指向数组的左右两端，它们可以容纳的水量为 \min(1, 7) * 8 = 8min(1,7)∗8=8。
        # 移动对应数字较小的那个指针（即此时的左指针），因为：
        # 容纳的水量 = 两个指针指向的高度中较小值 * 指针之间的距离
        # 如果移动数字较大的那个指针，那么前者「两个指针指向的数字中较小值」不会增加，后者「指针之间的距离」会减小，那么这个乘积会减
        # 小。因此，我们移动数字较大的那个指针是不合理的。因此，我们移动 数字较小的那个指针。

        s = 0
        i, j = 0, len(height)-1
        while i <= j:
            s = max(s, (j-i) * min(height[j], height[i]))
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return s
