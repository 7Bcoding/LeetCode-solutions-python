"""
Definition for singly-linked list.
给出两个非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0开头。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        headnode = ListNode(0)
        result = headnode
        carry = 0  # 进位

        while (l1 is not None) or (l2 is not None):
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            sumval = x + y + carry
            carry = sumval / 10
            result.next = ListNode(int(sumval % 10))
            result = result.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry >= 1:
            result.next = ListNode(int(carry))
        return headnode.next

