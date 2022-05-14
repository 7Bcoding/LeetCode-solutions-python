
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head, tail):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 解法：模拟
        # 1. 记录一个dummy.next为整个链表的头部，并需要4个指针：
        # pre，head，tail，post(head为翻转子链表头部，tail为翻转子链表尾部，
        # pre意义为子链表头部head的前一个节点，post为子链表尾部tail的后一个节点，
        # 初始pre和tail在同一起跑线，tail根据K的大小每次向前移动K步
        # 2. 每次翻转前，记录子链表head的前一个节点(pre)，以及记录子链表的后一个节点(post)
        # 3. 翻转head和tail组成的子链表(按照反转链表的3指针套路)，记录head为翻转链表尾部end，
        # 记录tail为翻转链表头部start，翻转后返回新的头和尾
        # 4. 把之前记录的的pre接上翻转后的子链表头，把翻转后子链表尾接上之前记录的post
        # 5. 循环，将子链表尾部的next作为新的head，将子链表尾部作为新的pre，即pre = tail，head = tail.next
        # 6. 循环边界条件：tail为空时，结束循环，返回dummy.next，head为空时，结束循环，返回dummy.next头结点

        start, end = tail, head
        tail.next = None
        pre, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        return start, end

    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            post = tail.next
            # 翻转子链表，按照翻转链表的套路即可
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = post
            pre = tail
            head = tail.next

        return dummy.next