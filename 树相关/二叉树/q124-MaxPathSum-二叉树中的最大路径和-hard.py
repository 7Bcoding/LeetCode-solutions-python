class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 解题思路：
        # 1. 使用一个列表来记录以每个节点的最大路径和
        # 2. dfs计算每个节点的最大路径和：
        #    最大路径和可能为：
        #    a. root.val
        #    b. 左节点的最大值 + root.val
        #    c. 右节点的最大值 + root.val
        #    d. 左节点最大值 + 右节点最大值 + root.val
        # 3. 每次返回时，应返回不带重复节点的最大值到父节点层级，因此仅返回:
        #    a. root.val
        #    b. 左节点最大值 + root.val
        #    c. 右节点的最大值 + root.val
        if not root:
            return None
        if not root.left and not root.right:
            return root.val
        max_list = []
        self.path_sum(root, max_list)
        print(max_list)
        return max(max_list)

    def path_sum(self, root, max_list):
        if not root:
            return 0
        if not root.left and not root.right:
            max_list.append(root.val)
            return root.val
        left_val = self.path_sum(root.left, max_list)
        right_val = self.path_sum(root.right, max_list)
        max_val = max(root.val, left_val + root.val, right_val + root.val, left_val + right_val + root.val)
        max_list.append(max_val)
        return max(root.val, left_val + root.val, right_val + root.val)