import collections


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # 个人解法：深度优先遍历 + 剪枝
        # visited标记是否访问过该节点，0——未从该节点出发进行过dfs，1——正在dfs该节点，2——该节点不安全，3——该节点最终安全
        # 如果visited=1 或 visited=2，则说明访问了深度遍历过程中访问过的节点或者访问了不安全的节点，则返回False，该节点不安全
        if len(graph) == 0: return []
        visited = [0] * len(graph)
        safenodes = []

        def dfsGraph(u):
            visited[u] = 1
            for v in graph[u]:
                if visited[v] == 0:
                    if not dfsGraph(v):
                        visited[v] = 2
                        return False
                elif visited[v] == 1 or visited[v] == 2:
                    return False
            visited[u] = 3
            return True

        for i in range(len(graph)):
            if not visited[i]:
                if not dfsGraph(i):
                    visited[i] = 2
                else:
                    visited[i] = 3
                    safenodes.append(i)
            elif visited[i] == 3 and i not in safenodes: safenodes.append(i)

        return safenodes

    # 官方解法：拓扑排序
    # 1. 分析
    #   对于一个节点 u，如果我们从 u 开始任意行走能够走到一个环里，那么 u 就不是一个安全的节点。换句话说，u 是一个安全的节点，
    # 当且仅当 u 直接相连的节点（u 的出边相连的那些节点）都是安全的节点。
    #   因此我们可以首先考虑没有任何出边的节点，它们一定都是安全的。随后我们再考虑仅与这些节点直接相连的节点，它们也一定是安全的，
    # 以此类推。这样我们可以将所有的边全部反向，首先所有没有任何入边的节点都是安全的，我们把这些节点全部移除。随后新的图中没有
    # 任何入边的节点都是安全的，以此类推。我们发现这种做法实际上就是对图进行拓扑排序。
    # 2. 算法
    #   我们将所有的边反向，得到反向图 rgraph，随后将 rgraph 中所有没有入边的节点加入队列中。每一次我们取出队列中的一个节点 u，
    # 将它从图中删除，如果此时某个节点 v 存在从 u 到 v 的一条边，并且在删掉了这条边后，v 变成了没有入边的节点，那么就把 v 加入
    # 队列。以此类推，直到队列为空。最后所有加入过队列的节点即为安全的节点。

    def eventualSafeNodes(self, graph):
        N = len(graph)
        safe = [False] * N

        graph = map(set, graph)
        rgraph = [set() for _ in range(N)]
        q = collections.deque()

        for i, js in enumerate(graph):
            if not js:
                q.append(i)
            for j in js:
                rgraph[j].add(i)

        while q:
            j = q.popleft()
            safe[j] = True
            for i in rgraph[j]:
                graph[i].remove(j)
                if len(graph[i]) == 0:
                    q.append(i)

        return [i for i, v in enumerate(safe) if v]
