class Solution(object):
    def findSmallestSetOfVertices(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # 解法：哈希表
        # 其实就是找没有入度的点
        # 1. 先遍历edges邻接关系表，将所有边的起点和终点加入字典中
        # 2. 起点首次出现在字典中 value = 0，终点首次出现 value = 1
        # 3. 节点再次出现在字典中 value + 1
        # 4. 最后再遍历一次字典的key，那些值为0的就是只作为起点出现过的节点，加入结果集
        if len(edges) == 0: return []
        vdict = dict()
        res = []
        for i in range(len(edges)):
            if edges[i][0] not in vdict:
                vdict[edges[i][0]] = 0
            if edges[i][1] not in vdict:
                vdict[edges[i][1]] = 1
            else:
                vdict[edges[i][1]] += 1
        for k in vdict.keys():
            if vdict[k] == 0:
                res.append(k)
        return res