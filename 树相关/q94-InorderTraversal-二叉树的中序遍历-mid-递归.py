class Solution(object):

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []

        def dfs(root):
            if not root:
                return
            # 按照 左-打印-右的方式遍历
                dfs(root.left)
                res.append(root.val)
                dfs(root.right)
        dfs(root)
        return res

