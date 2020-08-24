class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # 若 root 是 p, q 的 最近公共祖先 ，则只可能为以下情况之一：
        # 1. p 和 q 在 root 的子树中，且分列 root 的 异侧（即分别在左、右子树中）；
        # 2. p = root ，且 q 在 root 的左或右子树中；
        # 3. q = root ，且 p 在 root 的左或右子树中；
        # 考虑通过递归对二叉树进行后序遍历，当遇到节点 pp 或 qq 时返回。从底至顶回溯，
        # 当节点 p, q 在节点 root 的异侧时，节点 root 即为最近公共祖先，则向上返回 root 。
        # 递归解析：
        # 终止条件：
        # 1. 当越过叶节点，则直接返回 nullnull ；
        # 2. 当 root 等于 p, q ，则直接返回 root ；
        # 递推工作：
        # 1. 开启递归左子节点，返回值记为 left ；
        # 2. 开启递归右子节点，返回值记为 right ；
        # 返回值： 根据 left 和 right ，可展开为四种情况；
        # 1. 当 left 和 right 同时为空 ：说明 root 的左 / 右子树中都不包含 p,q ，返回 null ；
        # 2. 当 left 和 right 同时不为空 ：说明 p, q 分列在 root 的 异侧 （分别在 左 / 右子树），
        #    因此 root 为最近公共祖先，返回 root ；
        # 3. 当 left 为空 ，right 不为空 ：p, q 都不在 root 的左子树中，直接返回 right 。具体可分为两种情况：
        #   1. p, q 其中一个在 root 的 右子树 中，此时 right 指向 p (假设为 p)；
        #   2. p, q 两节点都在 root 的 右子树 中，此时的 right 指向 最近公共祖先节点 ；
        # 4. 当 left 不为空 ， right 为空 ：与情况 3. 同理；

        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left: return right
        if not right: return left
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