class Solution(object):
    def minimumSwap(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        if not s1 and not s2:
            return 0
        elif (s1.count('x') + s2.count('x')) % 2 != 0:
            return -1
        s1 = list(s1)
        s2 = list(s2)
        count = 0
        n = len(s1)
        for i in range(n):
            if s1[i] != s2[i]:
                for j in range(n - 1, -1, -1):
                    if s2[j] != s1[i] and s2[j] != s1[j]:
                        s1[i], s2[j] = s2[j], s1[i]
                        count += 1
                        break
            if s1 == s2:
                break
        return count

