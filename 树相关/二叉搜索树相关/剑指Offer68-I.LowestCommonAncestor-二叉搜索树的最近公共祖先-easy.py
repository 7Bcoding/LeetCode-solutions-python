class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # 解法：递归
        # 1. 当 p, q 都在 root 的 右子树 中，则开启递归 root.right 并返回
        # 2. 否则，当 p, q 都在 root 的 左子树 中，则开启递归 root.left 并返回
        # 3. 否则，返回最近公共祖先root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

    def lowestCommonAncestor(self, root, p, q):
        # 解法：迭代
        # 循环搜索： 当节点 root 为空时跳出；
        # 当 p, q 都在 root 的 右子树 中，则遍历至 root.right ；
        # 否则，当 p, q 都在 root 的 左子树 中，则遍历至 root.left ；
        # 否则，说明找到了最近公共祖先root ，跳出并返回root。
        while root:
            if root.val < p.val and root.val < q.val:  # p,q 都在 root 的右子树中
                root = root.right  # 遍历至右子节点
            elif root.val > p.val and root.val > q.val:  # p,q 都在 root 的左子树中
                root = root.left  # 遍历至左子节点
            else:
                break
        return root

    def lowestCommonAncestor(self, root, p, q):
        # 个人解法：路径公共节点
        # 1. dfs遍历两个节点分别得到两节点路径
        # 2. 求解公共节点
        def dfs(root, route, target):
            if not root: return route
            if root == target:
                route.append(root)
                return route
            route = dfs(root.left, route, target)
            if len(route) > 0:
                route.append(root)
                return route
            route = dfs(root.right, route, target)
            if len(route) > 0:
                route.append(root)
            return route

        route_p = dfs(root, [], p)
        route_q = dfs(root, [], q)

        for i in range(len(route_p)):
            if route_p[i] in route_q:
                return route_p[i]


