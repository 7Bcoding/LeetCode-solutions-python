
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 解法：深度遍历 + 记忆化搜索
        # 1. 首先后序遍历二叉树，深度遍历所有左子树根节点的右节点，不断往右走，直至最后一个右节点，将其返回
        #    node = dfsrightnode(root.left)
        # 2. 再将右子树根节点接到左子树最后一个右节点的下面，作为它的右子节点
        #    node.right = root.right
        # 3. 将左子树根节点接到根节点的下面，作为它的右子节点
        #    root.right = root.left
        # 最后返回的根节点即为所求
        if root is None: return None

        def dfsTree(root):
            if root is None:
                return None
            root.left = dfsTree(root.left)
            root.right = dfsTree(root.right)
            if root.left:
                node = dfsrightnode(root.left)
                node.right = root.right
                root.right = root.left
                root.left = None
            return root

        def dfsrightnode(root):
            if root.right is None:
                return root
            node = dfsrightnode(root.right)
            return node

        return dfsTree(root)





