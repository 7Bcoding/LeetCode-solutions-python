class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # 解法：迭代
        #
        if not root:
            return []
        stack = []
        res = []
        prev = None
        while root and stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right and root.right == prev:     # 右节点为空，直接打印中节点(加入res)
                res.append(root.val)
                prev = root
                root = None
            else:                                         # 右节点不为空，将弹出的中节点重新加入栈中，并继续往右走
                stack.append(root)
                root = root.right
        return res