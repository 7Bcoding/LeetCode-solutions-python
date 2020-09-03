class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        rdict = dict()
        res = []
        for i in range(len(rounds)-1):
            j = rounds[i]
            while j != rounds[i+1]:
                if j not in rdict:
                    rdict[j] = 1
                else:
                    rdict[j] += 1
                j += 1
                if j > n: j = 0
        if j not in rdict:
            rdict[j] = 1
        else:
            rdict[j] += 1

        rlist = sorted(rdict.items(), key=lambda item: item[1], reverse=True)
        print(rlist)
        for key in rdict.keys():
            if rdict[key] < rlist[0][1]:
                continue
            else:
                res.append(key)
        if 0 in res: res.remove(0)
        return res