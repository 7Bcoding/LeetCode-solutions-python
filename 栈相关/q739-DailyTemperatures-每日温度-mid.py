class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        # 典型单调栈
        n = len(T)
        ans, nxt, big = [0] * n, dict(), 10**9
        for i in range(n - 1, -1, -1):
            warmer_index = min(nxt.get(t, big) for t in range(T[i] + 1, 102))
            if warmer_index != big:
                ans[i] = warmer_index - i
            nxt[T[i]] = i
        return ans