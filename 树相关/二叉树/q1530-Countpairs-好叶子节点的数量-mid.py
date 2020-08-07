
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        给你二叉树的根节点 root 和一个整数 distance 。
        如果二叉树中两个 叶 节点之间的 最短路径长度 小于或者等于 distance ，那它们就可以构成一组 好叶子节点对 。
        返回树中 好叶子节点对的数量 。
        """
        # 解法：深度优先遍历(后续遍历) + 记忆化
        #   计算各个叶子节点之间的距离，本质上还是通过记录节点的深度+递归来求解
        # 可以使用后序遍历来获取每个节点的左子树和右子树满足条件的叶子节点数量：
        # 1. 递归左(右)子树，获取到叶子节点的距离，若满足条件则存入叶子节点距离列表中，
        # 递归边界条件：遇到叶子节点时返回[0]，表示存在一个满足条件的叶子节点(因为是叶子，所以距离为0）
        # 2. 上层节点获取到左右子树根节点的满足条件的叶子节点列表leftlist和rightlist，分别遍历距离值，
        # 若满足小于distance，则将该叶子节点的距离+1，加入本节点的叶子节点距离列表goodleaf中，然后返
        # 回goodleaf到上一层，上层继续循环该操作；
        # 3. 之后遍历左右子树根节点的叶子节点距离值列表，两两配对计算距离的和，小于distance的情况下，
        # 总的好叶子节点对数good+1

        def dfstree(root, good):
            if not root:
                return []
            if not root.left and not root.right:
                return [0]
            goodleaf = []
            leftlist = dfstree(root.left, good)    # 后序遍历来获取每个节点的左子树和右子树满足条件的叶子节点数量
            for i in leftlist:
                if i > distance:
                    continue
                goodleaf.append(i + 1)          # 该叶子节点的距离+1，更新至本节点的叶子节点距离列表中
            rightlist = dfstree(root.right, good)
            for i in rightlist:
                if i > distance:
                    continue
                goodleaf.append(i + 1)
            for l in leftlist:                      # 遍历左右子树根节点的叶子节点距离值列表，两两配对计算距离的和
                for r in rightlist:
                    if l + r + 2 <= distance:
                        good[0] += 1                   # 总的好叶子节点对数good+1
            return goodleaf
        good = [0]
        dfstree(root, good)
        return good[0]
