class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        示例 1:
        输入: [[1,3], [0,2], [1,3], [0,2]]
        输出: true
        解释:
        无向图如下:
        0----1
        |    |
        |    |
        3----2  我们可以将节点分成两组: {0, 2} 和 {1, 3}。
        """
        # 解法：深度优先搜索，遍历邻接节点：
        # 1.遇到未标记的节点，标记与上一个邻接节点不同的值A或B
        # 2.遇到标记过的节点，若与上一个邻接节点值相同，则无法满足条件，返回False
        #   若不同，则继续循环遍历邻接节点

        if len(graph) == 0: return False
        graphgroup = []
        for i in range(len(graph)):
            if graph[i]:
                graphgroup.append('N')
            else:
                graphgroup.append('empty')

        flag = True

        def deepsearchGraph(i, flag):
            for g in graph[i]:
                print(g, end=' ')
                if graphgroup[g] == 'N':
                    if graphgroup[i] == 'A':
                        graphgroup[g] = 'B'
                        flag = deepsearchGraph(g, flag)
                    else:
                        graphgroup[g] = 'A'
                        flag = deepsearchGraph(g, flag)
                elif graphgroup[g] == graphgroup[i]:
                    flag = False
                    return flag
                else:
                    continue
            return flag

        for i in range(len(graphgroup)):
            if graphgroup[i] == 'N':
                flag = deepsearchGraph(i, flag)

        return flag

