import collections


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 算法：拓扑排序 深度优先搜索
        # 对于图中的任意一个节点，它在搜索的过程中有三种状态，即：
        # 1. 「未搜索」：我们还没有搜索到这个节点
        # 2. 「搜索中」：我们搜索过这个节点，但还没有回溯到该节点，即该节点还没有入栈，还有相邻的节点没有搜索完成）
        # 3. 「已完成」：我们搜索过并且回溯过这个节点，即该节点已经入栈，并且所有该节点的相邻节点都出现在栈的更底部的位置，满足拓扑排序的要求
        #
        # 通过上述的三种状态，我们就可以给出使用深度优先搜索得到拓扑排序的算法流程，在每一轮的搜索搜索开始时，我们任取一个「未搜索」的节点开始进行深度优先搜索。
        # 我们将当前搜索的节点 u 标记为「搜索中」——visited[u]=1，遍历该节点的每一个相邻节点 v：
        # 1. 如果 v 为「未搜索」，visited[u]=0，那么我们开始搜索 v，待搜索完成回溯到 u；
        # 2. 如果 v 为「搜索中」，visited[u]=1，那么我们就找到了图中的一个环，因此是不存在拓扑排序的；
        # 3. 如果 v 为「已完成」，visited[u]=2，那么说明 v 已经在栈中了，而 u 还不在栈中，因此 u 无论何时入栈都不会影响到(u,v) 之前的拓扑关系，以及不用进行任何操作。
        # 当 u 的所有相邻节点都为「已完成」时，我们将 u 放入栈中，并将其标记为「已完成」。
        # 在整个深度优先搜索的过程结束后，如果我们没有找到图中的环，那么栈中存储这所有的 n 个节点，从栈顶到栈底的顺序即为一种拓扑排序。
        # 由于我们只需要判断是否存在一种拓扑排序，而栈的作用仅仅是存放最终的拓扑排序结果，因此我们可以只记录每个节点的状态，而省去对应的栈。

        edges = collections.defaultdict(list)
        visited = [0] * numCourses          # 标记是否访问过，0为没访问过，1为以该节点为起点进行深度遍历中，2为深度遍历该节点后没有发现环
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])  # 邻接表形式存储节点关系

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2                    # 以该节点为出发点进行深度遍历后，没有环
            result.append(u)                  # 以该节点出发，进行深度遍历后没有找到环，将节点加入拓扑排序的栈

        for i in range(numCourses):
            if valid and not visited[i]:      # 以某一节点出发，访问的图中没有找到环，继续找下一个没访问过的节点
                dfs(i)

        return valid
