import heapq
from queue import PriorityQueue


class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # 解法：prim算法 + 堆
        res, mincost = [], 0
        costs = [[0] * len(points) for _ in range(len(points))]
        for i in range(len(points)):
            for j in range(len(points)):
                costs[i][j] = abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])  # 计算曼哈顿距离
        selected = [0]
        candidate = [i for i in range(len(points))]
        cost_weight = [(0, 0)]   # 边权值和边的末尾节点
        while candidate:
            minweight, start = heapq.heappop(cost_weight)          # 弹出当前最小权值的边和该边结尾的点，以该点为起点继续寻找最小边
            if start not in candidate:                        # 已访问过的直接跳过
                continue
            selected.append(start)                            # 加入已访问节点集合中
            candidate.remove(start)                           # 从候选节点集合中移除该节点
            mincost += minweight                              # 更新最小权值总和
            for end in candidate:
                heapq.heappush(cost_weight, (costs[start][end], end))  # 获取以该节点为起点，到候选节点集合中剩余节点的边权值，加入堆中
        return mincost

    def minCostConnectPoints(self, points):
        # 解法：prim算法 + 优先队列
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