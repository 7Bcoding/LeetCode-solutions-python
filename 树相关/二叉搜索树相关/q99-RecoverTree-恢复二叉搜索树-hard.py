class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        # 解法：隐式中序遍历
        # 通过中序遍历，找到两个不满足递增顺序的节点，一个为pre,一个为root，
        # 获取到这两个node节点本身，然后进行值交换即可

        node = [None, None, None]  # prev, fisrt, second

        def dfs(root):
            if not root: return
            dfs(root.left)
            if node[0] and node[0].val > root.val:  # 第一次出现前一个元素比当前元素大
                node[2] = root  # 确定第二元素，其为较小值，即当前节点root的值
                if not node[1]:
                    node[1] = node[0]  # 确定第一元素，其为较大值，即prev的值
                else:
                    return
            node[0] = root  # prev随遍历向后移动
            dfs(root.right)

        dfs(root)
        node[1].val, node[2].val = node[2].val, node[1].val

