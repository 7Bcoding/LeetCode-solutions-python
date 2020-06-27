class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isSymmetricalTree(root.left, root.right)

    def isSymmetricalTree(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val == root2.val:
            return self.isSymmetricalTree(root1.left, root2.right) and self.isSymmetricalTree(root1.right, root2.left)
        else:
            return False

