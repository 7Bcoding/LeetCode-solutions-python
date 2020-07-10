class Trie:
    def __init__(self):
        self.root = {}

    def make_trie(self, words):
        root = self.root
        for word in words:
            currentdict = root
            for i in range(len(word)-1, -1, -1):
                currentdict = currentdict.setdefault(word[i], {})
            currentdict['_end'] = True


class Solution(object):
    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        输入：dictionary = ["looked","just","like","her","brother"]
             sentence = "jesslookedjustliketimherbrother"
        输出： 7
        """
        # 解法：字典树 + 动态规划
        # 动态规划：dp[i]表示前i个字符的最少未匹配字符数
        # 状态转移方程：
        # 1.外层循环
        # dp[i] = dp[i]+1 ——匹配串每新增一个字符，dp[i]的值为它前一个字符的最少匹配字符数dp[i]+1
        # 2.内层循环：
        # dp[i] = min(dp[i], dp[j]) ——匹配串的sentence[j:i-1]部分与字典中单词匹配，更新dp[i]的值，
        # 除去匹配的单词串部分，将单词串之前的最少未匹配字符数更新至dp[i]
        n = len(sentence)
        dp = [0] * (n+1)
        trie = Trie()
        trie.make_trie(dictionary)
        for i in range(1, n+1):
            dp[i] = dp[i-1] + 1
            currentdict = trie.root
            for j in range(i-1, -1, -1):
                currentdict = currentdict.get(sentence[j], None)
                if currentdict is None:
                    break
                elif currentdict.get('_end', False):
                    dp[i] = min(dp[i], dp[j])
        return dp[n]
