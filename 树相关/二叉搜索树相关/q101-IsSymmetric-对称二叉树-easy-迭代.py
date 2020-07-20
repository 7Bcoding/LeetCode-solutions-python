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
        node_stack = []
        if root.left and root.right:
            node_stack.append(root.left)
            node_stack.append(root.right)
        while node_stack:
            left = node_stack.pop(0)
            right = node_stack.pop(0)
            # 先判断非空
            if not right and not left:
                continue
            if not right or not left:
                return False
            # 都非空，再判断值是否相等
            if left.val != right.val:
                return False
            node_stack.append(left.left)
            node_stack.append(right.right)
            node_stack.append(left.right)
            node_stack.append(right.left)
        return True

