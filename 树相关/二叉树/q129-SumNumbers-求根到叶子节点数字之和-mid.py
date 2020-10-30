class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 解法：回溯算法
        res = []
        arr = []

        def sumtree(root):
            if not root:
                arr.append('')
                return 0
            arr.append(str(root.val))
            if not root.left and not root.right:
                res.append(int(''.join(arr[:])))
                return
            sumtree(root.left)
            arr.pop()
            sumtree(root.right)
            arr.pop()
            return False
        sumtree(root)
        return 0 if len(res) == 0 else sum(res)