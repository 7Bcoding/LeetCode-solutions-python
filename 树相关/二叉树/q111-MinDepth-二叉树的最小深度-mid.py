class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 解法：递归————深度优先遍历
        if not root: return 0

        def dfs(root, depth, mindepth):
            if not root:
                return min(mindepth, depth - 1)
            mindepth = dfs(root.left, depth + 1, mindepth)
            mindepth = dfs(root.right, depth + 1, mindepth)
            return mindepth

        mindepth = dfs(root, 1, float('inf'))

        return mindepth

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 解法：迭代————广度优先遍历
        if not root: return 0
        stack = [(root, 1)]
        mindepth = float('inf')
        while stack:
            root, depth = stack.pop()
            if not root.left and not root.right:
                mindepth = min(mindepth, depth)
            if root.left:
                stack.append((root.left, depth + 1))
            if root.right:
                stack.append((root.right, depth + 1))

        return mindepth