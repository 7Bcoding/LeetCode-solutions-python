from collections import defaultdict, deque


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        subseq = []
        if len(nums) == 0: return []

        # 解法：深度优先搜索 + 哈希表

        def dfs(pre, index):
            subset = set()
            for i in range(index, len(nums)):
                if (pre, i) in subset:
                    continue
                if nums[i] >= nums[pre]:
                    subset.add((pre, i))
                    subseq.append(nums[i])
                    if len(subseq) > 1 and subseq[:] not in res:
                        res.append(subseq[:])
                    dfs(i, i + 1)
                    if subseq: subseq.pop()
                else:
                    dfs(pre, i + 1)

        for i in range(len(nums)):
            dfs(i, i)
        return res

    def findSubsequences(self, nums):
        res = []
        d = deque([(nums, [])])
        while d:
            cur, new = d.popleft()
            if len(new) > 1:
                res.append(new)
            curPres = defaultdict(int)
            for inx, i in enumerate(cur):
                if curPres[i]:
                    continue
                if not new or i >= new[-1]:
                    curPres[i] = 1
                    d.append((cur[inx + 1:], new + [i]))
        return res




