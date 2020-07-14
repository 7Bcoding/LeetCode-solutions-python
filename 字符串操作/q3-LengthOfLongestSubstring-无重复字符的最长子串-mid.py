class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        repset = set()
        n = len(s)
        p, ans = -1, 0
        for i in range(n):
            if i != 0:
                repset.remove(s[i - 1])
            while p+1 < n and s[p + 1] not in repset:
                repset.add(s[p + 1])
                p += 1
            ans = max(ans, p - i + 1)
        return ans
