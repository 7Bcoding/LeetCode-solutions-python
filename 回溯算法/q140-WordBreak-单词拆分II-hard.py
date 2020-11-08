from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict):
        """s
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        # 解法：记忆化搜索
        # 对于字符串 s，如果某个前缀是单词列表中的单词，则拆分出该单词，然后对 s 的剩余部分继续拆分。
        # 如果可以将整个字符串 s 拆分成单词列表中的单词，则得到一个句子。在对 s 的剩余部分拆分得到一个
        # 句子之后，将拆分出的第一个单词（即 s 的前缀）添加到句子的头部，即可得到一个完整的句子。
        # 上述过程可以通过回溯实现。
        # 假设字符串 s 的长度为 n，回溯的时间复杂度在最坏情况下高达 O(n^n)。时间复杂度高的原因是存在
        # 大量重复计算，可以通过记忆化的方式降低时间复杂度。
        # 具体做法是，使用哈希表存储字符串 s 的每个下标和从该下标开始的部分可以组成的句子列表，在回溯过程
        # 中如果遇到已经访问过的下标，则可以直接从哈希表得到结果，而不需要重复计算。如果到某个下标发现无法
        # 匹配，则哈希表中该下标对应的是空列表，因此可以对不能拆分的情况进行剪枝优化。
        # 还有一个可优化之处为使用哈希集合存储单词列表中的单词，这样在判断一个字符串是否是单词列表中的单词
        # 时只需要判断该字符串是否在哈希集合中即可，而不再需要遍历单词列表。

        @lru_cache(None)
        def backtrack(index):
            if index == len(s):
                return [[]]
            ans = list()
            for i in range(index + 1, len(s) + 1):
                word = s[index:i]
                if word in wordSet:
                    nextWordBreaks = backtrack(i)
                    for nextWordBreak in nextWordBreaks:
                        ans.append(nextWordBreak.copy() + [word])
            return ans

        wordSet = set(wordDict)
        breakList = backtrack(0)
        return [" ".join(words[::-1]) for words in breakList]
