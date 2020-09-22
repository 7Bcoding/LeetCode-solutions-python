class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 解法：递归
        # 1. 用flag标记当前节点为其父节点的左子节点或右子节点
        # 2. 先序遍历二叉树，遇到左右子节点均为空，且为左子节点的节点，
        # 将其值加入到res中
        # 3. 最终对res求和即可
        if not root:
            return 0

        def dfs(root, flag, res):
            if not root.left and not root.right and flag == 'left':
                res += root.val
                return
            if root.left:
                dfs(root.left, 'left', res)
            if root.right:
                dfs(root.right, 'right', res)

        res = 0
        dfs(root, '', res)
        return sum(res)