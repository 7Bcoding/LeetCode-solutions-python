class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        if root is not None:
            stack.append((1, root))

        maxdepth = 0
        while stack:
            depth, root = stack.pop()
            maxdepth = max(depth, maxdepth)
            depth += 1
            if root.left:
                stack.append((depth, root.left))
            if root.right:
                stack.append((depth, root.right))

        return maxdepth