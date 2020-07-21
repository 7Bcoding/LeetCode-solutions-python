
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        # 解法：
        # 1.二叉搜索树关键的性质是根节点的值大于左子树所有节点的值，小于右子树所有节点的值，且左子树和右子树也同样为二叉搜索树。
        # 因此在生成所有可行的二叉搜索树的时候，假设当前序列长度为 nn，如果我们枚举根节点的值为 ii，那么根据二叉搜索树的性质
        # 我们可以知道左子树的节点值的集合为 [i-1][1...i−1]，右子树的节点值的集合为 [i+1 ... n][i+1...n]。
        # 而左子树和右子树的生成相较于原问题是一个序列长度缩小的子问题，因此我们可以想到用递归的方法来解决这道题目。
        #
        # 2.我们定义 generateTrees(start, end) 函数表示当前值的集合为[start,end]，返回序列 [start,end]
        # 生成的所有可行的二叉搜索树。按照上文的思路，我们考虑枚举[start,end] 中的值 i 为当前二叉搜索树的根，
        # 那么序列划分为了[start,i−1] 和 [i+1,end] 两部分。我们递归调用这两部分，即 generateTrees(start, i - 1) 和
        # generateTrees(i + 1, end)，获得所有可行的左子树和可行的右子树，那么最后一步我们只要从可行左子树集合中选一棵，
        # 再从可行右子树集合中选一棵拼接到根节点上，并将生成的二叉搜索树放入答案数组即可。
        #

        def generateTrees(start, end):
            if start > end:
                return [None, ]

            allTrees = []
            for i in range(start, end + 1):  # 枚举可行根节点
                # 获得所有可行的左子树集合
                leftTrees = generateTrees(start, i - 1)

                # 获得所有可行的右子树集合
                rightTrees = generateTrees(i + 1, end)

                # 从左子树集合中选出一棵左子树，从右子树集合中选出一棵右子树，拼接到根节点上
                for l in leftTrees:
                    for r in rightTrees:
                        currTree = TreeNode(i)
                        currTree.left = l
                        currTree.right = r
                        allTrees.append(currTree)

            return allTrees

        return generateTrees(1, n) if n else []

