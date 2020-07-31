class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0: return 0
        rainstack = [(-1,-1)]
        lastx, res, sumH = 0, 0, 0
        tmpH = []
        maxH = float('-inf')
        for i in range(len(height)):
            while height[i] > rainstack[-1][1] != -1:
                x, h = rainstack.pop()
                maxH = max(maxH, h)
                lastx = x
                tmpH.append(h)
            if rainstack[-1][1] != -1:
                lastx = rainstack[-1][0]
                maxH = rainstack[-1][1] if maxH == 0 else max(maxH, rainstack[-1][1])
            rainstack.append((i, height[i]))
            if tmpH:
                tmpH.pop()
                sumH = sum(tmpH)
            if maxH != float('-inf'):
                res += ((i-lastx-1) * maxH - sumH)
            maxH, sumH, tmpH = min(maxH, height[i]), 0, []
        return res


if __name__ == '__main__':
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    res = solution.trap(height)
    print(res)
    height = [1, 0, 0, 1]
    res = solution.trap(height)
    print(res)
