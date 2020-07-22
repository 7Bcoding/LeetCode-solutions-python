class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = []
        current = []
        sorted(candidates)

        def dfscombination(start, sumnums):
            if start > len(candidates): return
            for i in range(start, len(candidates)):
                while sumnums < target:
                    sumnums += candidates[i]
                    current.append(candidates[i])
                if sumnums == target:
                    result.append(current[:])
                if current:
                    current.pop()
                    sumnums -= candidates[i]
                dfscombination(i+1, sumnums)

        dfscombination(0, 0)
        return result


if __name__ == '__main__':
    solution = Solution()
    candidates = [2, 3, 5]
    target = 8
    result = solution.combinationSum(candidates, target)
    print(result)