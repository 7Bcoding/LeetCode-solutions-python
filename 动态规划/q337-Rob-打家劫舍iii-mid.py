class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 每个节点可选择偷或者不偷两种状态，根据题目意思，相连节点不能一起偷
        #
        # 1. 当前节点选择偷时，那么两个孩子节点就不能选择偷了
        # 2. 当前节点选择不偷时，两个孩子节点只需要拿最多的钱出来就行(两个孩子节点偷不偷没关系)
        # 我们使用一个大小为 2 的数组来表示 result = [] ———— 0 代表不偷，1 代表偷
        # 任何一个节点能偷到的最大钱的状态可以定义为：
        # 1. 当前节点选择不偷———— 当前节点能偷到的最大钱数 = 左孩子能偷到的钱 + 右孩子能偷到的钱
        # 2. 当前节点选择偷———— 当前节点能偷到的最大钱数 = 左孩子选择自己不偷时能得到的钱 + 右孩子选择不偷时能得到的钱 + 当前节点的钱数

        if not root: return 0, 0
        ls, ln = self.rob(root.left)
        rs, rn = self.rob(root.right)

        return root.val + ln + rn, max(ls, ln) + max(rs, rn)

    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0, 0
        result = []
        left = self.rob(root.left)
        right = self.rob(root.right)
        result[0] = max(left[0], left[1]), max(right[0], right[1])
        result[1] = root.val + left[0] + right[0]
        return result