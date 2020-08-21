class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 解法：滑动窗口
        # 1. 取一个set为不重复字符的集合，快指针代表滑动窗口的右端点，慢指针代表左端点
        # 2. 快指针遇到不重复的字符往前走，并添加进入set集合，在遇到重复字符时退出循环
        # 3. 慢指针在遇到重复字符时，往前走一步，并从set集合中删除前一个重复字符
        # 4. 每次遇到重复字符退出循环时，计算滑动窗口左右端点的距离，更新无重复字符子串最大长度
        repset = set()
        n = len(s)
        p, ans = -1, 0
        for i in range(n):
            if i != 0:
                repset.remove(s[i - 1])                 # 慢指针向前移动一步，并删除之前一个重复的字符
            while p+1 < n and s[p + 1] not in repset:   # 遇到重复字符时退出循环
                repset.add(s[p + 1])
                p += 1
            ans = max(ans, p - i + 1)                   # 更新无重复字符子串最大长度
        return ans
