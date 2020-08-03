class Solution(object):
    class Solution(object):
        def isSubPath(self, head, root):
            """
            :type head: ListNode
            :type root: TreeNode
            :rtype: bool
            """
            # 个人解法：递归，DFS，记忆化搜索

            def dfs_Treelist(root, head, listnode):
                if listnode is None: return True
                if root is None and listnode:
                    return False
                if root.val != listnode.val and listnode == head:
                    return dfs_Treelist(root.left, head, listnode) or \
                           dfs_Treelist(root.right, head, listnode)
                elif root.val != listnode.val and listnode != head:
                    return False
                elif root.val == listnode.val and listnode == head:
                    if dfs_Treelist(root.left, head, listnode.next) or \
                            dfs_Treelist(root.right, head, listnode.next):
                        return True
                    if dfs_Treelist(root.left, head, listnode) or \
                           dfs_Treelist(root.right, head, listnode):
                        return True
                return dfs_Treelist(root.left, head, listnode.next) or \
                       dfs_Treelist(root.right, head, listnode.next)

            return dfs_Treelist(root, head, head)

        # 官方解法

        def isSubPath(self, head, root):
            """
            :type head: ListNode
            :type root: TreeNode
            :rtype: bool
            """
            if not head:
                return True
            if not root:
                return False
            if root.val != head.val:
                return False

            return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)

        def isSubPath(self, head, root):
            if not root:
                return False
            if self.dfs(head, root):
                return True
            return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
