class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        stack = []
        while stack or root:
            # 不断往左子树方向走，每走一次就将当前节点保存到栈中
            # 这是模拟递归的调用
            if root:
                stack.append(root)
                root = root.left
            # 当前节点为空，说明左边走到头了，从栈中弹出节点并保存
            # 然后转向右边节点，继续上面整个过程
            else:
               tmp = stack.pop()
               res.append(tmp.val)
               root = tmp.right
        return res
