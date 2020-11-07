
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        # 解法：动态规划 先说说本题的常见误区，有人可能觉得我使用双指针left，right按顺序遍历字符串的子串，如果[left,
        # right]之间子串在字典中，那么，以该子串之后的第一个位置作为下一个子串的开始，同样，遍历下一个子串，直到right
        # 到达s的末尾。但是这样是错误的，考虑s='leetcode'，假如wordDict = ['leet'，'leetcode']，如果我们先遍历到leet
        # 子串，剩余部分是code，字典中没有，就认为该单词无法拆分，实际上wordDict直接就有leetcode，显然，这种策略是不正确的
        # 为了避免上述这种字典中存在长的能覆盖短的情形，让right从字符串右端开始向左滑动，以保证最长的拆分子串以及最少的拆分次
        # 数。那么，right从后面开始遍历就对了么，事实上，也是不对的，考虑s='abcd'，假如wordDict = ["a","abc","b","cd"]，
        # right从后边开始，我们先找到了abc，剩余的d就没有匹配的了，然而，我们是可以按照a+b+cd的组合匹配的，于是，right
        # 不管从头部还是从尾部开始，我们都无法解决问题，双指针是不行的。
        # 事实上这有点类似迷宫问题，我们先沿着一条路径走，最后发现找不到出口，那么就需要回过头看看是否还存在其他路径，因此，
        # 需要事先将每一轮所有的存在可能的路径都保存，然后，我们才能开始往下进行，如果存在走通的情形，那么，我们就找到了拆分
        # 的组合。但是我们回溯所有可能的情形如果遇到：
        # s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
        # wordDict=["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        # 存在可能的情形是呈指数式的暴涨，直接导致超时，这种情形，我们需要保存访问过的位置，这样，才不会回溯重复位置，回溯才
        # 不会超时。
        # 有没有更好的方法？我们不妨将s从长度为0逐渐拉长，如果每次都能通过前面的长度更短的能拆分的s+字典中存在的元素组成新的s
        # ，那么长度为i的单词就可拆分，如果不能递推得到，说明长度为i的s不能拆分，这就是动态规划的思想，转移方程为：
        # dp[i] = dp[j] & checkdict(s[j,i])
        #
        l = len(s)
        if not wordDict: return not s
        dp = [False] * (l + 1)
        dp[0] = True
        for i in range(1, l + 1):
            for j in range(i - 1, -1, -1):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
