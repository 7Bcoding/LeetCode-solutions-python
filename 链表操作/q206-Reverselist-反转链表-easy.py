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
        # 解法1：三指针
        # 1. 一个指针做临时节点，负责将pre往前进一步
        # 2. 一个指针为pre，负责将cur往前进一步
        # 3. 一个指针为cur，始终在pre前一个，负责将pre的next指向前一个节点
        cur, pre = None, head
        while pre:
            tmp = pre.next
            pre.next = cur
            cur = pre
            pre = tmp
        return cur

    def reverseList(self, head):
        # 解法2：两次遍历
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
