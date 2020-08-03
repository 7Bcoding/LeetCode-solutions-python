
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right


class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        if root is None or head is None: return False
        nodelist = []

        def dfs_Treelist(root, head, listnode, nodelist):
            if listnode is None: return True
            if root is None and listnode:
                return False
            if root.val != listnode.val and listnode == head:
                flag = dfs_Treelist(root.left, head, listnode, nodelist)
                flag = dfs_Treelist(root.right, head, listnode, nodelist)
            elif root.val != listnode.val and listnode != head:
                return False
            else:
                nodelist.append(root.val)
                flag = dfs_Treelist(root.left, head, listnode.next, nodelist)
                if flag: return True
                if nodelist: nodelist.pop()
                flag = dfs_Treelist(root.right, head, listnode.next, nodelist)
                if flag: return True
                if nodelist: nodelist.pop()
            return flag

        flag = dfs_Treelist(root.right, head, head, nodelist)
        print(nodelist)
        return flag


if __name__ == '__main__':
    solution = Solution()
    root = TreeNode(1, TreeNode(4, None, TreeNode(2, TreeNode(1, None, None), None)),
                    TreeNode(4, TreeNode(2, TreeNode(6, None, None), TreeNode(8, TreeNode(1, None, None), TreeNode(3, None, None))), None))
    list = [1,4,2,6,8]
    node = ListNode(0)
    dummy = ListNode(0)
    dummy.next = node
    for i in range(len(list)):
        node.val = list[i]
        node.next = ListNode(0)
        node = node.next
    node = dummy.next
    for i in range(len(list)):
        print(node.val, end='')
        node = node.next
    res = solution.isSubPath(dummy.next, root)
    print(res)