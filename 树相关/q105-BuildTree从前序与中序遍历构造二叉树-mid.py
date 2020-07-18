class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        前序遍历 preorder = [3,9,1,6,20,15,7]
        中序遍历 inorder = [1,9,6,3,15,20,7]
              3
            /  \
           9   20
          / \  / \
         1  6 15  7
        """

        n = len(preorder)

        def BuildBinaryTree(preleft, preright, inleft, inright):
            if preleft > preright:
                return None

            # 前序遍历中的第一个节点就是根节点
            preroot = preleft
            # 在中序遍历中定位根节点
            inroot = inorder.index(preorder[preroot])

            # 先把根节点建立出来
            root = TreeNode(preorder[preroot])
            # 得到左子树中的节点数目
            size_left_subtree = inroot - inleft

            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = BuildBinaryTree(preleft + 1, size_left_subtree+preleft, inleft, inroot - 1)

            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = BuildBinaryTree(size_left_subtree+preleft + 1, preright, inroot + 1, inright)

            return root

        return BuildBinaryTree(0, n - 1, 0, n - 1)