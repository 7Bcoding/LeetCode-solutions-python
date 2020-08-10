class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        lstr = list(str)
        for i in range(len(lstr)):
            if 65 <= ord(lstr[i]) <= 90:
                lstr[i] = chr(ord(str[i]) + 32)
        return ''.join(lstr)