class TreeNode(object):
    def __init__(self, x=0, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        res_tree = []
        while queue:
            root = queue.pop(0)
            if root:
                res_tree.append(root.val)
                queue.append(root.left)
                queue.append(root.right)
            else:
                res_tree.append(None)
        for i in range(len(res_tree) - 1, -1, -1):
            if res_tree[i] is None:
                res_tree.pop(i)
            else:
                break

        return ''.join(str(res_tree))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """





if __name__ == '__main__':
    solution = Codec()
    print(solution.serialize(
        TreeNode(1, TreeNode(2, None, None), TreeNode(3, TreeNode(4, None, None), TreeNode(5, None, None)))))
    print(solution.serialize(
        TreeNode(1, TreeNode(2, TreeNode(4, None, None), TreeNode(5, None, None)), TreeNode(3, None, None))))
