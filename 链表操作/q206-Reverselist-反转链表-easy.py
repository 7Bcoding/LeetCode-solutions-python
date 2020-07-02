class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        nodestack = []
        node = head
        while node:
            nodestack.append(node)
            node = node.next
        dummy = ListNode()
        dummy.next = nodestack.pop()
        n = dummy.next
        while n != head:
            n.next = nodestack.pop()
            n = n.next
        n.next = None
        return dummy.next