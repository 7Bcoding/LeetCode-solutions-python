import collections
import heapq


class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        # 解法：欧拉回路————Hierholzer算法
        # Hierholzer 算法用于在连通图中寻找欧拉路径，其流程如下：
        # 1. 从起点出发，进行深度优先搜索。
        # 2. 每次沿着某条边从某个顶点移动到另外一个顶点的时候，都需要删除这条边。
        # 3. 如果没有可移动的路径，则将所在节点加入到栈中，并返回。
        #   当我们顺序地考虑该问题时，我们也许很难解决该问题，因为我们无法判断当前节点的哪一个分支是「死胡同」分支。
        #   不妨倒过来思考。我们注意到只有那个入度与出度差为 11 的节点会导致死胡同。而该节点必然是最后一个遍历到的节点。
        # 我们可以改变入栈的规则，当我们遍历完一个节点所连的所有节点后，我们才将该节点入栈（即逆序入栈）。
        #   对于当前节点而言，从它的每一个非「死胡同」分支出发进行深度优先搜索，都将会搜回到当前节点。而从它的「死胡同」
        # 分支出发进行深度优先搜索将不会搜回到当前节点。也就是说当前节点的死胡同分支将会优先于其他非「死胡同」分支入栈。
        #   这样就能保证我们可以「一笔画」地走完所有边，最终的栈中逆序地保存了「一笔画」的结果。我们只要将栈中的内容反转，
        # 即可得到答案。

        def dfs(curr):
            while vec[curr]:
                tmp = heapq.heappop(vec[curr])
                dfs(tmp)
            stack.append(curr)

        vec = collections.defaultdict(list)
        for depart, arrive in tickets:
            vec[depart].append(arrive)
        for key in vec:
            heapq.heapify(vec[key])

        stack = list()
        dfs("JFK")
        return stack[::-1]
