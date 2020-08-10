class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0: return ''
        i = 1
        slist = list(s)
        while i < len(slist)-1:
            if len(slist) > 0 and abs(ord(slist[i]) - ord(slist[i - 1])) == 32:
                slist.pop(i - 1)
                slist.pop(i - 1)
                i = 1
            else:
                i += 1
        i = 0
        while i < len(slist)-1:
            if len(slist) > 0 and abs(ord(slist[i+1]) - ord(slist[i])) == 32:
                slist.pop(i)
                slist.pop(i)
                i = 0
            else:
                i += 1
        return ''.join(slist)