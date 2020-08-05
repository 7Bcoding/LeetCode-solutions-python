class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        cache = dict()
        # -- 暴力递归-最优子结构
        # 在解法一和解法二中，使用爷爷、两个孩子、4 个孙子来说明问题
        # 首先来定义这个问题的状态：爷爷节点获取到最大的偷取的钱数
        # 1. 首先要明确相邻的节点不能偷，也就是爷爷选择偷，儿子就不能偷了，但是孙子可以偷
        # 2. 二叉树只有左右两个孩子，一个爷爷最多 2 个儿子，4 个孙子
        # 根据以上条件，我们可以得出单个节点的钱该怎么算
        # 4 个孙子偷的钱 + 爷爷的钱 VS 两个儿子偷的钱 哪个组合钱多，就当做当前节点能偷的最大钱数。这就是动态规划里面的最优子结构
        # 1. 4个孙子投的钱加上爷爷的钱如下
        # method1 = root.val + rob(root.left.left) + rob(root.left.right) + rob(root.right.left) + rob(root.right.right)
        # 2. 两个儿子偷的钱如下
        # method2 = rob(root.left) + rob(root.right)
        # 3. 挑选一个钱数多的方案则
        # result = max(method1, method2)

        # --  记忆化(缓存)优化
        # 针对解法一种速度太慢的问题，经过分析其实现，我们发现爷爷在计算自己能偷多少钱的时候，同时计算了 4 个孙子能偷多少钱，也计算了 2 个儿子能偷多少钱。
        # 这样在儿子当爷爷时，就会产生重复计算一遍孙子节点。于是乎我们发现了一个动态规划的关键优化点：
        # --  重复子问题
        # 我们这一步针对重复子问题进行优化，我们在做斐波那契数列时，使用的优化方案是记忆化，但是之前的问题都是使用数组解决的，把每次计算的结果都存起来，下次
        # 如果再来计算，就从缓存中取，不再计算了，这样就保证每个数字只计算一次。由于二叉树不适合拿数组当缓存，我们这次使用哈希表来存储结果，TreeNode当做key，能偷的钱当做value

        def dfs_robTree(root, cache):
            if not root: return 0
            if root in cache.keys(): return cache[root]
            money = root.val
            if root.left:
                money += dfs_robTree(root.left.left, cache) + dfs_robTree(root.left.right, cache)
            if root.right:
                money += dfs_robTree(root.right.left, cache) + dfs_robTree(root.right.left, cache)
            maxmoney = max(money, dfs_robTree(root.left, cache), dfs_robTree(root.right, cache))
            cache[root] = maxmoney
            return maxmoney
        return dfs_robTree(root, cache)

