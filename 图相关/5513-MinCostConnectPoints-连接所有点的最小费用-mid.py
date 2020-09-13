from queue import PriorityQueue


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 解法：正常的prim算法（超时）
        res, mincost = [], 0
        cost = [[0] * len(points) for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(len(points)):
                cost[i][j] = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])
        seleted_node = [0]
        candidate_node = [i for i in range(1, len(points))]
        while candidate_node:
            begin, end, minweight = 0, 0, float('inf')
            for i in seleted_node:
                for j in candidate_node:
                    if cost[i][j] < minweight:
                        minweight = cost[i][j]
                        end = j
            mincost += minweight
            seleted_node.append(end)
            candidate_node.remove(end)

        return mincost

    def minCostConnectPoints(self, points):
        # 解法：prim + 优先队列
        cal = lambda p1, p2: abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])  # 计算曼哈顿距离
        pq = PriorityQueue()
        visited = set([i for i in range(len(points))])
        res = 0
        pq.put((0, 0))  # (distance, point_id)
        while visited:
            dis, now = pq.get()  # (到扩展集中某最近点的距离，某最近点的序号)
            if now not in visited:  # 已访问过的直接跳过
                continue
            visited.remove(now)  # 随手剪枝
            res += dis
            for i in visited:
                pq.put((cal(points[now], points[i]), i))  # 按距离丢进优先队列排序就好，无须构建边结构

        return res