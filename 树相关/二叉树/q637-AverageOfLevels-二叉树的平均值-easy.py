import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        # 解法1：深度优先遍历
        # 使用深度优先搜索计算二叉树的层平均值，需要维护两个数组，counts 用于存储二叉树的
        # 每一层的节点数，sums 用于存储二叉树的每一层的节点值之和。搜索过程中需要记录当前
        # 节点所在层，如果访问到的节点在第 i 层，则将 counts[i]的值加 1，并将该节点的值加到 sums[i]。
        def dfs(root, level):
            if not root:
                return
            if level < len(totals):
                totals[level] += root.val
                counts[level] += 1
            else:
                totals.append(root.val)
                counts.append(1)
            dfs(root.left, level + 1)
            dfs(root.right, level + 1)

        counts = list()
        totals = list()
        dfs(root, 0)
        return [total / count for total, count in zip(totals, counts)]

    def averageOfLevels(self, root):
        # 解法2：广度优先遍历
        # 也可以使用广度优先搜索计算二叉树的层平均值。从根节点开始搜索，每一轮遍历同一层的全部节点，
        # 计算该层的节点数以及该层的节点值之和，然后计算该层的平均值。
        # 如何确保每一轮遍历的是同一层的全部节点呢？我们可以借鉴层次遍历的做法，广度优先搜索使用队列
        # 存储待访问节点，只要确保在每一轮遍历时，队列中的节点是同一层的全部节点即可。具体做法如下：
        # 1. 初始时，将根节点加入队列；
        # 2. 每一轮遍历时，将队列中的节点全部取出，计算这些节点的数量以及它们的节点值之和，并计算这些节点
        # 的平均值，然后将这些节点的全部非空子节点加入队列，重复上述操作直到队列为空，遍历结束。
        # 由于初始时队列中只有根节点，满足队列中的节点是同一层的全部节点，每一轮遍历时都会将队列中的当前
        # 层节点全部取出，并将下一层的全部节点加入队列，因此可以确保每一轮遍历的是同一层的全部节点。
        # 具体实现方面，可以在每一轮遍历之前获得队列中的节点数量 size，遍历时只遍历 size 个节点，即可满足
        # 每一轮遍历的是同一层的全部节点。
        averages = list()
        queue = collections.deque([root])
        while queue:
            total = 0
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                total += node.val
                left, right = node.left, node.right
                if left:
                    queue.append(left)
                if right:
                    queue.append(right)
            averages.append(total / size)
        return averages

