class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addtwonumbers(self, l1, l2):

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 解法：
        # 本题的主要难点在于链表中数位的顺序与我们做加法的顺序是相反的，
        # 为了逆序处理所有数位，我们可以使用栈：把所有数字压入栈中，再依次取出相加
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        head = None
        carry = 0  # 进位
        while s1 or s2 or carry != 0:
            x = s1.pop() if s1 else 0
            y = s2.pop() if s2 else 0
            sumval = x + y + carry
            carry = sumval // 10
            pre = ListNode(sumval % 10)
            pre.next = head
            head = pre
        return head