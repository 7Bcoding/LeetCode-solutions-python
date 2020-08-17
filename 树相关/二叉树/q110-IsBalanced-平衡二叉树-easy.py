class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 解法：递归————自顶向下
        # height(p)= 0 ，p 是空节点
        # height(p)= max(height(p.left),height(p.right))+1 ，p 是非空节点
        # 有了计算节点高度的函数，即可判断二叉树是否平衡。具体做法类似于二叉树的前序遍历，即对于当前遍历到的节点，
        # 首先计算左右子树的高度，如果左右子树的高度差是否不超过 11，再分别递归地遍历左右子节点，并判断左子树和右
        # 子树是否平衡。这是一个自顶向下的递归的过程。
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(
            root.right)

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 解法：递归————自底向上
        # 方法一由于是自顶向下递归，因此对于同一个节点，函数height会被重复调用，导致时间复杂度较高。如果使用自底向上的做法，则对于
        # 每个节点，函数height只会被调用一次。
        # 自底向上递归的做法类似于后序遍历，对于当前遍历到的节点，先递归地判断其左右子树是否平衡，再判断以当前节点为根的子树是否
        # 平衡。如果一棵子树是平衡的，则返回其高度（高度一定是非负整数），否则返回 -1−1。如果存在一棵子树不平衡，则整个二叉树一定不平衡。

        def height(root):
            if not root:
                return 0
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1
            else:
                return max(leftHeight, rightHeight) + 1

        return height(root) >= 0
