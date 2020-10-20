class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root):
        # 解法：中序遍历
        # 考虑对升序数组 a 求任意两个元素之差的绝对值的最小值，答案一定为相邻两个元素之差的最小值
        # 其他任意间隔距离大于等于 2 的下标对 (i,j) 的元素之差一定大于下标对 (i,i+1) 的元素之差，故不需要再被考虑。
        # 二叉搜索树有个性质为二叉搜索树中序遍历得到的值序列是递增有序的，因此我们只要得到中序遍历后的值序列即能用上
        # 文提及的方法来解决。朴素的方法是经过一次中序遍历将值保存在一个数组中再进行遍历求解，我们也可以在中序遍历的
        # 过程中用 pre 变量保存前驱节点的值，这样即能边遍历边更新答案，不再需要显式创建数组来保存，需要注意的是 pre 的
        # 初始值需要设置成任意负数标记开头，下文代码中设置为 -1。

        def dfs(root):
            nonlocal res, pre
            if not root:
                return
            dfs(root.left)
            if pre != -1:
                res = min(res, root.val - pre)
            pre = root.val
            dfs(root.right)

        pre = -1
        res = float('inf')
        dfs(root)
        return res

