class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 解法1：反向中序遍历序列
        # 由题意可知，其实就是求解二叉搜索树的单调递减序列的逐项累加值，并在对应节点上更改。
        # 已知二叉搜索树的中序遍历是一个单调递增的有序序列。
        # 如果我们反序地中序遍历该二叉搜索树，即可得到一个单调递减的有序序列。
        # 本题中要求我们将每个节点的值修改为原来的节点值加上所有大于它的节点值之和。
        # 这样我们只需要反序中序遍历该二叉搜索树，记录过程中的节点值之和，并不断更新当前遍历到
        # 的节点的节点值，即可得到题目要求的累加树。
        def dfs(root):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)

        total = 0
        dfs(root)
        return root

    def convertBST(self, root):
        # 解法2：Morris 遍历
        # 有一种巧妙的方法可以在线性时间内，只占用常数空间来实现中序遍历。这种方法由 J. H. Morris 在 1979 年
        # 的论文「Traversing Binary Trees Simply and Cheaply」中首次提出，因此被称为 Morris 遍历。
        # Morris 遍历的核心思想是利用树的大量空闲指针，实现空间开销的极限缩减。其反序中序遍历规则总结如下：
        # 1. 如果当前节点的右子节点为空，处理当前节点，并遍历当前节点的左子节点；
        # 2. 如果当前节点的右子节点不为空，找到当前节点右子树的最左节点（该节点为当前节点中序遍历的前驱节点）；
        #  -- 如果最左节点的左指针为空，将最左节点的左指针指向当前节点，遍历当前节点的右子节点；
        #  -- 如果最左节点的左指针不为空，将最左节点的左指针重新置为空（恢复树的原状），处理当前节点，并将当前节点置为其左节点；
        # 3. 重复步骤 1 和步骤 2，直到遍历结束。
        # 这样我们利用 Morris 遍历的方法，反序中序遍历该二叉搜索树，即可实现线性时间与常数空间的遍历。
        def getSuccessor(node):
            succ = node.right
            while succ.left and succ.left != node:
                succ = succ.left
            return succ

        total = 0
        node = root

        while node:
            if not node.right:
                total += node.val
                node.val = total
                node = node.left
            else:
                succ = getSuccessor(node)
                if not succ.left:
                    succ.left = node
                    node = node.right
                else:
                    succ.left = None
                    total += node.val
                    node.val = total
                    node = node.left

        return root



