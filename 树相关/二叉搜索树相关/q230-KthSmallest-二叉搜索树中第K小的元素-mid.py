import heapq


class Solution(object):
    def kthSmallest(self, root, k):

        # 个人解法：使用Python堆模块heapq选出最小的前K个元素，返回列表最后一个数即可
        if root is None: return None
        nodelist = []

        def dfsTree(root):
            if root:
                nodelist.append(root.val)
                dfsTree(root.left)
                dfsTree(root.right)
        dfsTree(root)
        ksmall_list = heapq.nsmallest(k, nodelist)

        return ksmall_list[-1]

    # -- 怎么遍历树：
    # 1. 深度优先搜索（DFS）
    #   在这个策略中，我们从根延伸到某一片叶子，然后再返回另一个分支。根据根节点，左节点，右节点的相对顺序，DFS 还可以分为前序，中序，后序。
    # 2. 广度优先搜索（BFS）
    #   在这个策略中，我们逐层，从上到下扫描整个树。
    # -- 为了解决这个问题，可以使用 BST 的特性————BST 的中序遍历是升序序列。

    def kthSmallest(self, root, k):

        # -- 方法一：递归
        # 1.通过构造 BST 的中序遍历序列，则第 k-1 个元素就是第 k 小的元素。
        # 2.时间复杂度：O(N)，遍历了整个树。
        #   空间复杂度：O(N)，用了一个数组存储中序序列。

        def inorder(r):
            return inorder(r.left) + [r.val] + inorder(r.right) if r else []

        return inorder(root)[k - 1]

    def kthSmallest(self, root, k):

        # -- 方法二：迭代
        # 在栈的帮助下，可以将方法一的递归转换为迭代，这样可以加快速度，因为这样可以不用遍历整个树，可以在找到答案后停止。
        # 即栈中弹出第K个节点后，直接返回该节点的值(此处用K来做标记，每弹出一个元素，就将K减小1
        # 复杂度分析：
        # 1.时间复杂度：O(H+k)，其中 H 指的是树的高度，由于我们开始遍历之前，要先向下达到叶，当树是一个平衡树时：
        # 复杂度为O(logN+k)。当树是一个不平衡树时：复杂度为 O(N+k)，此时所有的节点都在左子树。
        # 2.空间复杂度：O(H+k)。当树是一个平衡树时：O(logN+k)。当树是一个非平衡树时：O(N+k)。

        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
