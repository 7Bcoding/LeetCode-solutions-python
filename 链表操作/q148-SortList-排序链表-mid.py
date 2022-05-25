# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def sortFunc(head, tail):
            """
            对链表进行排序
            """
            if not head:
                return None
            if head.next == tail:
                head.next = None
                return head
            slow = fast = head
            while fast != tail:
                slow = slow.next
                fast = fast.next
                if fast != tail:
                    fast = fast.next
            mid = slow
            return merge(sortFunc(head, mid), sortFunc(mid, tail))

        def merge(head, tail):
            """
            合并2个升序的子链表
            """
            dummy = ListNode(-1)
            temp, pHead1, pHead2 = dummy, head, tail
            while pHead1 and pHead2:
                if pHead1.val <= pHead2.val:
                    temp.next = pHead1
                    pHead1 = pHead1.next
                else:
                    temp.next = pHead2
                    pHead2 = pHead2.next
                temp = temp.next
            if pHead1:
                temp.next = pHead1
            if pHead2:
                temp.next = pHead2
            return dummy.next

        return sortFunc(head, None)
