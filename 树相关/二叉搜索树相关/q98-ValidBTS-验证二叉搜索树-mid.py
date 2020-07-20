class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.validBST(root, -2**32, 2**32-1)

    # 通过递归将节点的值传递到下一层，让每个节点都获取到它的最大值边界和最小值边界
    def validBST(self, root, small, large):
        if root is None:
            return True
        if small >= root.val or large <= root.val:
            return False
        return self.validBST(root.left, small, root.val) and self.validBST(root.right, root.val, large)
