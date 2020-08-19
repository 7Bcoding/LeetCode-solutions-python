class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # 解法：DFS + 分治
        # 1. 遍历链表，转换成列表
        # 2. 分治，不断二分查找取列表中间点做根节点
        if not head: return None
        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        def dfs(arr, low, high):
            if low > high: return None
            mid = low + (high - low) // 2
            root = TreeNode(arr[mid])
            root.left = dfs(arr, low, mid - 1)
            root.right = dfs(arr, mid + 1, high)
            return root

        return dfs(arr, 0, len(arr) - 1)
