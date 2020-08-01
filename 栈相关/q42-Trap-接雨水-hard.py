class Solution(object):
    def trap1(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 解法：单调栈
        # 产生凹陷的地方才能存储雨水，那么高度一定是先减后增，所以思路就是维护一个高度递减的 stack
        # 1. 凹陷的高度 = min( 栈顶柱子高度，加入的柱子高度 ) - 弹出的柱子高度
        # 如果凹陷部分弹出了柱子，则需要减掉柱子的高度
        # 2. 凹陷的长度 = 栈顶柱子下标 - 加入的柱子下标 - 1
        # 3. 凹陷区域大小 = 凹陷的长度 * 凹陷的高度
        # 4. 每弹出一个元素，计算一次结果
        if len(height) == 0: return 0
        stack, res, H = [], 0, 0
        for i in range(len(height)):
            while len(stack) > 0 and height[i] > height[stack[-1]]:
                top = stack.pop()
                if len(stack) == 0:
                    break
                H = min(height[i], height[stack[-1]]) - height[top]
                dist = i - stack[-1] - 1
                res += (dist * H)
            stack.append(i)

        return res

# 数学解法：
    def trap2(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 从左往右遍历，不管是雨水还是柱子，都计算在有效面积内，并且每次累加的值根据遇到的最高的柱子逐步上升。
        # 1. 从左往右遍历得S1，每步S1+=max1且max1逐步增大
        # 2. 从右往左遍历得S2，每步S2+=max2且max2逐步增大
        # 3. 然后S1 + S2会覆盖整个矩形，并且：重复面积 = 2倍柱子面积 + 2倍积水面积
        # 最终，积水面积 = S1 + S2 - 矩形面积(包含空白面积+1倍柱子+1倍积水) - 1倍柱子面积

        n = len(height)
        # 同时从左往右和从右往左计算有效面积
        s1, s2 = 0, 0
        max1, max2 = 0, 0
        for i in range(n):
            if height[i] > max1:
                max1 = height[i]
            if height[n - i - 1] > max2:
                max2 = height[n - i - 1]
            s1 += max1
            s2 += max2
        # 积水面积 = S1 + S2 - 矩形面积 - 柱子面积
        res = s1 + s2 - max1 * len(height) - sum(height)
        return res

