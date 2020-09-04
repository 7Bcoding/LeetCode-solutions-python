class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []

        def dfs(root, route):
            if not root: return
            route += str(root.val)
            if not root.left and not root.right:  # 当前节点是叶子节点
                res.append(route)                 # 把路径加入到答案中
            else:                                 # 当前节点不是叶子节点，继续递归遍历
                route += '->'
                dfs(root.left, route)
                dfs(root.right, route)

        dfs(root, '')
        return res
