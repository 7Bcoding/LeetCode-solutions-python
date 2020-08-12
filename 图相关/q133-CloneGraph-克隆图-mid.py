from collections import deque


class Node(object):
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution(object):

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        # 解法1：深度优先搜索
        # 1. 使用一个哈希表存储所有已被访问和克隆的节点。哈希表中的 key 是原始图中的节点，value 是克隆图中的对应节点。
        # 2. 从给定节点开始遍历图。如果某个节点已经被访问过，则返回其克隆图中的对应节点。
        # 3. 如果当前访问的节点不在哈希表中，则创建它的克隆节点并存储在哈希表中。注意：在进入递归之前，必须先创建克隆节点
        # 并保存在哈希表中。如果不保证这种顺序，可能会在递归中再次遇到同一个节点，再次遍历该节点时，陷入死循环。
        # 4. 递归调用每个节点的邻接点。每个节点递归调用的次数等于邻接点的数量，每一次调用返回其对应邻接点的克隆节点，最终返
        # 回这些克隆邻接点的列表，将其放入对应克隆节点的邻接表中。这样就可以克隆给定的节点和其邻接点。

        if not node:
            return node

        # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
        if node in self.visited:
            return self.visited[node]

        # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        clone_node = Node(node.val, [])

        # 哈希表存储
        self.visited[node] = clone_node

        # 遍历该节点的邻居并更新克隆节点的邻居列表
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node

        # 解法2：广度优先搜索
        #
        # 1. 使用一个哈希表 visited 存储所有已被访问和克隆的节点。哈希表中的 key 是原始图中的节点，value 是克隆图中的对应节点。
        # 2. 将给定的节点添加到队列。队列弹出节点 n，克隆该节点并存储到哈希表中。
        # 3. 每次从队列首部取出一个节点，遍历该节点的所有邻接点。如果某个邻接点已被访问，则该邻接点一定在 visited 中，那么从 visited
        # 获得该邻接点，否则创建一个新的节点存储在 visited 中，并将邻接点添加到队列。将克隆的邻接点添加到克隆图对应节点的邻接表中。
        # 注意：队列中的节点及其邻接表为浅拷贝，不能直接拷贝队列节点的neighbor到哈希表节点visited[n] 中，因为是深拷贝，所以仅从队列中
        # 获取邻接关系，在哈希表中操作对应节点visited[neighbor]更新邻接列表，即visited[n].neighbors.append(visited[neighbor])，
        # 所以每个节点在加入哈希表中时，其邻接列表必须为空。
        # 重复上述操作直到队列为空，则整个图遍历结束。

    def cloneGraph(self, node):
            """
            :type node: Node
            :rtype: Node
            """
            if not node:
                return node

            visited = {}

            # 将题目给定的节点添加到队列
            queue = deque([node])
            # 克隆第一个节点并存储到哈希表中
            visited[node] = Node(node.val, [])

            # 广度优先搜索
            while queue:
                # 取出队列的头节点
                n = queue.popleft()
                # 遍历该节点的邻居
                for neighbor in n.neighbors:
                    if neighbor not in visited:
                        # 如果没有被访问过，就克隆并存储在哈希表中
                        visited[neighbor] = Node(neighbor.val, [])
                        # 将邻居节点加入队列中
                        queue.append(neighbor)
                    # 更新当前节点的邻居列表
                    visited[n].neighbors.append(visited[neighbor])

            return visited[node]
