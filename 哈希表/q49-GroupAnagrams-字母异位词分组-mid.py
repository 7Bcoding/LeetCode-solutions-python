import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        输入: ["eat", "tea", "tan", "ate", "nat", "bat"]
        输出:
        [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
        ]
        """
        strdict = collections.defaultdict(list)
        for s in strs:
            strdict[tuple(sorted(s))].append(s)
        return strdict.values()

