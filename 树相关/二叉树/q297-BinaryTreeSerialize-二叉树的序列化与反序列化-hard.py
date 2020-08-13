class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root: return "[]"
        queue = [root]
        res_tree = []
        while queue:
            root = queue.pop(0)
            if root:
                res_tree.append(str(root.val))
                queue.append(root.left)
                queue.append(root.right)
            else:
                res_tree.append('null')
        for i in range(len(res_tree) - 1, -1, -1):
            if res_tree[i] is 'null':
                res_tree.pop(i)
            else:
                break
        return '[' + ','.join(res_tree) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        nodeval = data[1:-1].split(',')

        def dfs(i):
            if i > len(nodeval) - 1:
                return None
            if nodeval[i] != 'null':
                root = TreeNode(int(nodeval[i]))
                root.left = dfs(2 * i + 1)
                root.right = dfs(2 * i + 2)
            else:
                root = None
            return root
        return dfs(0)