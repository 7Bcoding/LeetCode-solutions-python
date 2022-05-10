# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None or left == right:
            return head
        revhead = head
        revhead_pre = revhead
        i = 1
        while i < left:
            revhead_pre = revhead
            revhead = revhead.next
            i += 1
        # 翻转链表原来的头
        pre = None
        curr = revhead
        j = left
        while curr != None and j <= right:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
            j += 1
        revhead.next = curr
        if left != 1:
            revhead_pre.next = pre
        else:
            head = pre

        return head