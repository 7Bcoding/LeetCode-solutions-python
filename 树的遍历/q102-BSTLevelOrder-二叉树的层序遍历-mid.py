class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return
        nodequeue = ["r", root]
        line = []
        result = []
        while nodequeue:
            node = nodequeue.pop(0)
            if isinstance(node, TreeNode):
                line.append(node.val)
                if node.left:
                    nodequeue.append(node.left)
                if node.right:
                    nodequeue.append(node.right)
            else:
                if len(nodequeue) > 0:
                    nodequeue.append("r")
                    result.append(line)
                    line = []
        return result



