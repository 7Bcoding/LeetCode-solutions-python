class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def Sorttree(left, right):
            if left > right:
                return None

            mid = (right+left) // 2
            root = TreeNode(nums[mid])

            root.left = Sorttree(left, mid - 1)
            root.right = Sorttree(mid + 1, right)
            return root

        return Sorttree(0, len(nums)-1)