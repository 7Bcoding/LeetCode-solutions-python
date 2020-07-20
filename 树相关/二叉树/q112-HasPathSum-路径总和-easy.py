class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False

        def hasPath(root, sumvalue):

            sumvalue += root.val
            if root.left:
                leftflag = hasPath(root.left, sumvalue)
            if root.right:
                rightflag = hasPath(root.right, sumvalue)
            if root.left is None and root.right is None:
                if sumvalue == sum:
                    return True
                else:
                    return False
            return leftflag or rightflag

        return hasPath(root, 0)