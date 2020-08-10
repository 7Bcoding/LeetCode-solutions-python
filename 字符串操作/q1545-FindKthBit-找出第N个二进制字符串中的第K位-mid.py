class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s = ['0']
        count = 1
        while count < n:
            rs = s[::-1]
            s += ['1']
            for i in range(len(rs)):
                if rs[i] == '0':
                    rs[i] = '1'
                else:
                    rs[i] = '0'
            s += rs
            count += 1

        return ''.join(s[k - 1])
