
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # 回溯算法 + 剪枝
        # 回溯边界条件——当组合元素个数达到K时，返回
        # 1.组合元素个数为0，还有K个元素待填时，循环最多走到n-k+2
        # 2.组合元素个数为1，还有K-1个元素待填时，最多走到n-(k-1)+2
        # 3.以此类推，组合元素个数为len(cbset)，还有K-len(cbset)个元素待填时,最多走到n - (k - len(cbset)) + 2
        # 以5个元素选3个为组合为例：
        # 剪枝：
        # 1.待填元素为3时，首个数字只有1,2,3, 3种可能，4往后是无意义的，剪掉
        # 2.待填元素为2时，最多走到4，x 4 5都可。而x 5无意义，剪掉
        # 3.待填元素为1时，最多走到5
        res = []
        def combinenums(num, cbset):

            if len(cbset) == k:
                res.append(cbset[:])
                return

            for i in range(num, n - (k - len(cbset)) + 2):
                cbset.append(i)
                combinenums(i+1, cbset)
                cbset.pop()
        combinenums(1, [])

        return res
